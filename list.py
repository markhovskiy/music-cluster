import sys
import os
import argparse

from utils.lister import Lister


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
  sys.exit("Path not found: {}".format(root_dir))

lister = Lister(args.color, args.tags)
lister.list(root_dir, 0, args.depth)
