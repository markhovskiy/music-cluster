import sys
import os

root_dir = os.path.expanduser(os.path.join('~', 'Music'))
if not os.path.exists(root_dir):
  sys.exit('Path not found: ' + root_dir)

depth = None if len(sys.argv) is 1 else int(sys.argv[1])

class effects:
  end = '\033[0m'
  bold = '\033[1m'
  colors = {
    'grey': '\033[90m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
  }

def effect_by_ext(ext):
  ext_effects = {
    'mp3': effects.colors['blue'],
    'jpg': effects.colors['yellow'],
    'jpeg': effects.colors['yellow'],
  }

  if not ext in ext_effects:
    return effects.colors['grey']

  return ext_effects[ext]

def list(dir_path, offset = 0, depth = None):
  if depth is 0:
    return

  for subfile_name in os.listdir(dir_path):
    subfile_path = os.path.join(dir_path, subfile_name)
    is_subfile_dir = os.path.isdir(subfile_path)
    effect = effects.bold if is_subfile_dir else effect_by_ext(os.path.splitext(subfile_name)[1][1:].lower())

    for i in range(0, offset):
      print('  ', end='')

    print(effect + subfile_name + effects.end)

    if is_subfile_dir:
      list(subfile_path, offset + 1, None if depth is None else (depth - 1))

list(root_dir, 0, depth)
