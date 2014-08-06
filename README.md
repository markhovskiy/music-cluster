# music-cluster

a set of cli utilities for dealing with a local music collection

### setup (dev)

1. [install "virtualenvwrapper"](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation)
2. create virtualenv for python2.7 (because mutagen can't really parse tags on python3): `mkvirtualenv --python=/usr/bin/python2.7 music-cluster`
3. `pip install -r requirements.txt`

then just `workon music-cluster`

### usage

``` bash
python list.py [-h] [-c] [-d DEPTH] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -c, --color           whether to color files by extensions
  -t, --tags            whether to print tags
  -d DEPTH, --depth DEPTH
                        restricts subfolders level
  -p PATH, --path PATH  defines path to list in, defaults to current dir
```
e.g. `python list.py -c -t -d 1 -p ~/Music/` will print something like:
```
Between the Buried and Me | 2006 | Alaska | Metal | 2 | Alaska | 4:58 | Alaska.mp3
```

### todo

* introduce file-based configs for patterns, colors etc.
* add renaming capabilities (by patterns)
* add search capabilities
* take advantage of last.fm stats

### links

* http://mutagen.readthedocs.org/en/latest/api/id3.html
