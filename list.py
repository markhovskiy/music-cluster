import sys
import os

root_dir = os.path.expanduser(os.path.join('~', 'Music'))
if not os.path.exists(root_dir):
  sys.exit('Path not found: ' + root_dir)

depth = None if len(sys.argv) is 1 else int(sys.argv[1])

def list(dir_path, offset = 0, depth = None):
  if depth is 0:
    return

  for subfile_name in os.listdir(dir_path):
    subdir_path = os.path.join(dir_path, subfile_name)

    for i in range(0, offset):
      print('  ', end='')

    print(subfile_name)

    if os.path.isdir(subdir_path):
      list(subdir_path, offset + 1, None if depth is None else (depth - 1))

list(root_dir, 0, depth)
