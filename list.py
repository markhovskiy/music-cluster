from __future__ import print_function
import sys
import os
import argparse
from mutagen.mp3 import MP3
import effects

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--color', action='store_true',
                    help='whether to color files by extensions')
parser.add_argument('-t', '--tags', action='store_true',
                    help='whether to print tags')
parser.add_argument('-d', '--depth', type=int,
                    help='restricts subfolders level')
parser.add_argument('-p', '--path',
                    help='defines path to list in, defaults to current dir')
args = parser.parse_args()

root_dir = os.path.abspath(args.path) if args.path else os.getcwd()
if not os.path.exists(root_dir):
  sys.exit('Path not found: ' + root_dir)

def get_file_ext(file_name):
  return os.path.splitext(file_name)[1][1:].lower()

def print_file_tags(file_path, separator = ' | '):
  audio = MP3(file_path)

  # (artist, year, album, title)
  for frame in ('TPE1', 'TDRC', 'TALB', 'TIT2'):
    if frame in audio:
      print(audio[frame].text[0], end=separator)

def print_file_data(file_path, file_name, is_subfile_dir):
  file_ext = get_file_ext(file_name)

  if args.tags and file_ext.lower() == 'mp3':
    print_file_tags(file_path)

  if not args.color:
    print(file_name)
    return

  effect = 'bold' if is_subfile_dir else effects.get_ext_color(file_ext)
  effects.print_with_effect(file_name, effect)

def list(dir_path, offset = 0, depth = None):
  if depth == 0:
    return

  for subfile_name in os.listdir(dir_path):
    subfile_path = os.path.join(dir_path, subfile_name)
    is_subfile_dir = os.path.isdir(subfile_path)

    print('  ' * offset, end='')
    print_file_data(subfile_path, subfile_name, is_subfile_dir)

    if is_subfile_dir:
      list(subfile_path, offset + 1, None if depth is None else (depth - 1))

list(root_dir, 0, args.depth)
