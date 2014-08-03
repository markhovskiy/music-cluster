from __future__ import print_function
import os
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

  def print_file_tags(self, file_path):
    audio = MP3(file_path)

    for frame in self.tag_frames:
      if frame in audio:
        print(audio[frame].text[0], end=self.tag_separator)

    print(self.format_duration(audio.info.length), end=self.tag_separator)

  def print_file_data(self, file_path, file_name, is_dir):
    file_ext = self.get_file_ext(file_name)

    if self.to_print_tags and file_ext.lower() == 'mp3':
      self.print_file_tags(file_path)

    if not self.to_color:
      print(file_name)
      return

    effect = 'bold' if is_dir else effects.get_ext_color(file_ext)
    effects.print_with_effect(file_name, effect)

  def list(self, dir_path, offset=0, depth=None):
    """Print file/folder data recursively"""
    if depth == 0:
      return

    for file_name in os.listdir(dir_path):
      file_path = os.path.join(dir_path, file_name)
      is_dir = os.path.isdir(file_path)

      print(' ' * self.offset_width * offset, end='')
      self.print_file_data(file_path, file_name, is_dir)

      if is_dir:
        self.list(file_path, offset + 1, None if depth is None else (depth - 1))
