from __future__ import print_function
import math
import os
import re

from mutagen.mp3 import MP3

import effects


class Lister:
    # number of spaces to indent (marking nesting)
    offset_width = 2

    # see http://id3.org/id3v2.4.0-frames
    tag_frames = (
        'TPE1',  # artist
        'TDRC',  # year
        'TALB',  # album
        'TCON',  # genre
        'TRCK',  # track number
        'TIT2',  # title
    )

    @staticmethod
    def format_duration(duration):
        mins = "{0:.0f}".format(math.floor(duration / 60))
        secs = "{0:.0f}".format(math.floor(duration % 60))
        if len(secs) == 1:
            secs = "0{0}".format(secs)
        return "{0}:{1}".format(mins, secs)

    @staticmethod
    def max_tags_width(files):
        tags_width = {}

        for file_data in files:
            if 'tags' not in file_data:
                continue

            for frame, tag in file_data['tags'].iteritems():
                width = len(tag)
                if width > tags_width.get(frame, 0):
                    tags_width[frame] = width

        return tags_width

    def __init__(self, to_disable_effects, to_print_tags):
        self.effects_enabled = not to_disable_effects
        self.to_print_tags = to_print_tags
        self.tag_separator = self.highlight(" | ", 'grey')

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
                print(self.highlight(file_name, 'bold'))

                self.list(file_path,
                          offset + 1,
                          None if depth is None else (depth - 1))
            else:
                file_ext = os.path.splitext(file_name)[1][1:].lower()
                file_data = dict(name=file_name, ext=file_ext)

                if self.to_print_tags and file_ext == 'mp3':
                    file_data['tags'] = self.collect_file_tags(file_path)

                files.append(file_data)

        folder_tags_width = self.max_tags_width(files)
        for file_data in files:
            self.print_offset(offset)
            self.print_file_data(file_data, folder_tags_width)

    def highlight(self, text, *effect):
        return effects.apply(text, *effect) if self.effects_enabled else text

    def collect_file_tags(self, file_path):
        audio = MP3(file_path)
        tags = {}

        for frame in self.tag_frames:
            if frame in audio:
                # e.g. "audio['TDRC']" has "ID3TimeStamp" type
                tag = unicode(audio[frame].text[0])

                # removing a "total" part (in case of "current/total" format)
                # and leading zeros
                if frame == 'TRCK':
                    tag = re.sub('^0*|/.*', "", tag)

                tags[frame] = tag

        tags['duration'] = self.format_duration(audio.info.length)

        return tags

    def print_offset(self, offset):
        print(" " * self.offset_width * offset, end="")

    def print_file_data(self, file_data, tags_width):
        if 'tags' in file_data:
            for frame in self.tag_frames + ('duration',):
                tag = file_data['tags'].get(frame, "")
                align = '>' if frame in ('TRCK', 'duration') else '<'
                width = tags_width.get(frame, 0)
                print(u"{0:{1}{2}}".format(tag, align, width),
                      end=self.tag_separator)

        print(self.highlight(file_data['name'],
                             effects.get_ext_color(file_data['ext'])))
