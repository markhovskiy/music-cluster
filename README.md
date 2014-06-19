# music-cluster

a set of cli utilities for dealing with a local music collection

### setup (dev)

1. [install "virtualenvwrapper"](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation)
2. create virtualenv for python3: `mkvirtualenv --python=/usr/bin/python3 music-cluster`
3. `pip install mutagen`

then just `workon music-cluster`

### usage

``` bash
python list.py [-h] [-c] [-d DEPTH] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -c, --color           whether to color files by extensions
  -d DEPTH, --depth DEPTH
                        restricts subfolders level
  -p PATH, --path PATH  defines path to list in, defaults to current dir
```
e.g. `python list.py -c -d 2 -p ~/Music/`

### todo

* utilize "mutagen" to print tags data
* introduce file-based configs for patterns, colors etc.
* add renaming capabilities (by patterns)
* add search capabilities
* take advantage of last.fm stats

### links

* http://mutagen.readthedocs.org/en/latest/api/id3.html
