from __future__ import print_function
import os
import re

from mutagen.mp3 import MP3

import effects


class Lister:
  # number of spaces to indent (marking nesting)
  offset_width = 2

  # see http://id3.org/id3v2.4.0-frames
  tag_frames = (
    'TPE1', # artist
    'TDRC', # year
    'TALB', # album
    'TCON', # genre
    'TRCK', # track number
    'TIT2', # title
  )

  tag_separator = ' | '

  def __init__(self, to_color, to_print_tags):
    self.to_color = to_color
    self.to_print_tags = to_print_tags

  def get_file_ext(self, file_name):
    return os.path.splitext(file_name)[1][1:].lower()

  def format_duration(self, duration):
    mins = "{0:.0f}".format(round(duration / 60))
    secs = "{0:.0f}".format(round(duration % 60))
    return "{0}:{1}".format(mins,
                            secs if len(secs) == 2 else "0{0}".format(secs))

  def collect_file_tags(self, file_path):
    audio = MP3(file_path)
    tags = {}

    for frame in self.tag_frames:
      if frame in audio:
        # normalizing to strings (e.g. "TDRC" is stored as "ID3TimeStamp")
        tag = u"{}".format(audio[frame].text[0])

        # taking only "current" part if value appears in "current/total" format
        # and removing preceding zeros
        if frame == 'TRCK':
          tag = re.sub('^0*|/.*', "", tag)

        tags[frame] = tag

    tags['duration'] = self.format_duration(audio.info.length)

    return tags

  def max_tags_width(self, files):
    tags_width = {}

    for file_data in files:
      if 'tags' not in file_data:
        continue

      for frame in file_data['tags']:
        width = len(file_data['tags'][frame])
        if width > tags_width.get(frame, 0):
          tags_width[frame] = width

    return tags_width

  def print_file_tags(self, tags, tags_width):
    for frame in self.tag_frames + ('duration',):
      print(u"{0:{align}{width}}".format(tags.get(frame, ""),
                                         align='>' if frame in ('TRCK', 'duration') else '<',
                                         width=tags_width.get(frame, 0)),
            end=self.tag_separator)

  def print_offset(self, offset):
    print(" " * self.offset_width * offset, end="")

  def print_file_data(self, file_data, offset, tags_width):
    self.print_offset(offset)

    if 'tags' in file_data:
      self.print_file_tags(file_data['tags'], tags_width)

    if self.to_color:
      effects.print_with_effect(file_data['file_name'],
                                effects.get_ext_color(file_data['file_ext']))
    else:
      print(file_data['file_name'])

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
        effects.print_with_effect(file_name, 'bold')

        self.list(file_path,
                  offset + 1,
                  None if depth is None else (depth - 1))
      else:
        file_ext = self.get_file_ext(file_name)
        file_data = dict(file_name=file_name,
                         file_ext=file_ext)

        if self.to_print_tags and file_ext.lower() == 'mp3':
          file_data['tags'] = self.collect_file_tags(file_path)

        files.append(file_data)

    folder_tags_width = self.max_tags_width(files)
    for file_data in files:
      self.print_file_data(file_data, offset, folder_tags_width)
