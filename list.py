import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--depth', type=int, help='restricts subfolders level')
args = parser.parse_args()

root_dir = os.path.expanduser(os.path.join('~', 'Music'))
if not os.path.exists(root_dir):
  sys.exit('Path not found: ' + root_dir)

effects = {
  'end': '\033[0m',
  'bold': '\033[1m',
  'colors': {
    'grey': '\033[90m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
  }
}

def get_ext_color(ext):
  ext_colors = {
    'mp3': 'blue',
    'jpg': 'yellow',
    'jpeg': 'yellow',
  }

  color = ext_colors[ext] if ext in ext_colors else 'grey'

  return effects['colors'][color]

def get_file_ext(file_name):
  return os.path.splitext(file_name)[1][1:].lower()

def list(dir_path, offset = 0, depth = None):
  if depth is 0:
    return

  for subfile_name in os.listdir(dir_path):
    subfile_path = os.path.join(dir_path, subfile_name)
    is_subfile_dir = os.path.isdir(subfile_path)
    effect = effects['bold'] if is_subfile_dir else get_ext_color(get_file_ext(subfile_name))

    for i in range(0, offset):
      print('  ', end='')

    print(effect + subfile_name + effects['end'])

    if is_subfile_dir:
      list(subfile_path, offset + 1, None if depth is None else (depth - 1))

list(root_dir, 0, args.depth)
