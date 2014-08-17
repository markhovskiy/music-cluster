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
e.g. `python list.py -p ~/Music/ -c -t` will print something like:
![screenshot](https://raw.githubusercontent.com/markhovskiy/markhovskiy.github.io/master/uploads/music_cluster_screenshot.png)

### todo

* order by file name
* add functionality for checking a file tree against tags (e.g. `"<artist>" -> "<year> - <album>" -> "<track number> - <title>.mp3"`)
* introduce file-based configs for patterns, colors etc.
* add renaming capabilities (by patterns)
* add search capabilities
* take advantage of last.fm stats (e.g. http://www.last.fm/api/show/track.getTags)

### links

* http://mutagen.readthedocs.org/en/latest/api/id3.html
