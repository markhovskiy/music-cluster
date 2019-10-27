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
parser.add_argument("-v", "--validate", action='store_true',
                    help="if filename matches tags, paints it green")
parser.add_argument("-d", "--depth", type=int,
                    help="restricts level of subfolders")
args = parser.parse_args()

root_dir = os.path.abspath(args.path)
if not os.path.exists(root_dir):
    sys.exit(f"Path not found: {root_dir}")

lister = Lister(to_disable_effects=args.plain,
                to_print_tags=args.tags,
                to_validate=args.validate)
lister.list(root_dir, 0, args.depth)
