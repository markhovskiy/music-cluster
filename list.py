import sys
import os
import argparse

from utils.lister import Lister


parser = argparse.ArgumentParser()
parser.add_argument("path",
                    help="path to list in")
parser.add_argument("-t", "--tags", action='store_true',
                    help="whether to print tags")
parser.add_argument("-p", "--plain", action='store_true',
                    help="plain text mode, effects disabled (colors, bold)")
parser.add_argument("-d", "--depth", type=int,
                    help="restricts level of subfolders")
args = parser.parse_args()

root_dir = os.path.abspath(args.path)
if not os.path.exists(root_dir):
  sys.exit("Path not found: {}".format(root_dir))

lister = Lister(args.plain, args.tags)
lister.list(root_dir, 0, args.depth)
