from __future__ import print_function
import os
import re

from mutagen.mp3 import MP3

import effects
import formatters


class FileData:
    def __init__(self, name):
        self.name = name
        self.ext = os.path.splitext(name)[1][1:].lower()
        self.tags = {}

    def is_mp3(self):
        return self.ext == 'mp3'

    def has_tags(self):
        return len(self.tags) > 0

    def has_valid_name(self):
        valid_filename = u"{:0>2} - {}.{}".format(self.tags.get('TRCK', ''),
                                                  self.tags.get('TIT2', ''),
                                                  self.ext)

        return unicode(self.name, 'utf-8') == valid_filename


class Lister:
    # number of spaces to indent (marking nesting)
    offset_length = 2

    # see http://id3.org/id3v2.4.0-frames
    tag_frames = ('TPE1',  # artist
                  'TDRC',  # year
                  'TALB',  # album
                  'TCON',  # genre
                  'TRCK',  # track number
                  'TIT2')  # title

    @staticmethod
    def max_tags_length(files):
        tags_length = {}

        for file_data in files:
            for frame, tag in file_data.tags.iteritems():
                length = len(tag)
                if length > tags_length.get(frame, 0):
                    tags_length[frame] = length

        return tags_length

    def __init__(self,
                 to_disable_effects=False,
                 to_print_tags=False,
                 to_validate=False):
        self.effects_enabled = not to_disable_effects
        self.to_print_tags = to_print_tags
        self.to_validate = to_validate
        self.tag_separator = self.highlight(u" \u2758 ", 'grey')

    def list(self, dir_path, offset=0, depth=None):
        """
        Prints file/folder data recursively

        To have all tags printed in columns (by folders):
        collecting each file data and printing all of them afterwards.
        """

        if depth == 0:
            return

        files = []

        for file_name in sorted(os.listdir(dir_path)):
            file_path = os.path.join(dir_path, file_name)

            if os.path.isdir(file_path):
                self.print_offset(offset)
                print(self.highlight(unicode(file_name, 'utf-8'),
                                     'bold'))

                self.list(file_path,
                          offset + 1,
                          None if depth is None else depth - 1)

                continue

            file_data = FileData(file_name)

            if self.to_print_tags and file_data.is_mp3():
                file_data.tags = self.collect_file_tags(MP3(file_path))

            files.append(file_data)

        folder_tags_length = self.max_tags_length(files)
        for file_data in files:
            self.print_offset(offset)
            self.print_file_data(file_data, folder_tags_length)

    def highlight(self, text, *effect):
        return effects.apply(text, *effect) if self.effects_enabled else text

    def get_filename_color(self, file_data):
        return 'green' if (all([self.to_validate,
                                file_data.is_mp3(),
                                file_data.has_tags(),
                                file_data.has_valid_name()])) else \
               effects.get_ext_color(file_data.ext)

    def collect_file_tags(self, audio):
        return dict({frame: self.retrieve_tag(audio, frame)
                     for frame in self.tag_frames
                     if frame in audio},
                    **{'duration': formatters.to_time_str(audio.info.length)})

    def retrieve_tag(self, audio, frame):
        # e.g. "audio['TDRC']" has "ID3TimeStamp" type
        tag = unicode(audio[frame].text[0])

        # removing a "total" part (in case of "current/total" format)
        # and leading zeros
        if frame == 'TRCK':
            tag = re.sub('^0*|/.*', "", tag)

        return tag

    def print_offset(self, offset):
        print(" " * self.offset_length * offset, end="")

    def print_file_data(self, file_data, tags_length):
        if file_data.has_tags():
            for frame in self.tag_frames + ('duration',):
                tag = file_data.tags.get(frame, "")
                align = '>' if frame in ('TRCK', 'duration') else '<'
                length = tags_length.get(frame, 0)

                print(u"{0:{1}{2}}".format(tag, align, length),
                      end=self.tag_separator)

        print(self.highlight(unicode(file_data.name, 'utf-8'),
                             self.get_filename_color(file_data)))
