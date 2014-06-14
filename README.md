# music-cluster

a set of cli utilities for dealing with a local music collection

### usage

``` bash
python3 list.py [-h] [-d DEPTH] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        restricts subfolders level
  -p PATH, --path PATH  defines path to list in, defaults to current dir
  -c, --color           whether to color files by extensions
```
e.g. `python3 list.py -c -d 2 -p ~/Music/`

### todo

* utilize "mutagen" to print tags data
* introduce file-based configs for patterns, colors etc.
* add renaming capabilities (by patterns)
* add search capabilities
* take advantage of last.fm stats

### links

* https://code.google.com/p/mutagen/
