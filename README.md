# music-cluster

[![Build Status](https://api.travis-ci.org/markhovskiy/music-cluster.svg)](https://travis-ci.org/markhovskiy/music-cluster)

a cli utility for dealing with local music collections


### setup (dev)

1. [install "virtualenvwrapper"](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation)
2. create virtualenv for python2.7 (because mutagen can't really parse tags on python3): `mkvirtualenv --python=/usr/bin/python2.7 music-cluster`
3. `pip install -r requirements.txt`
4. `workon music-cluster`


### testing

```bash
py.test utils/tests/

```


### usage

``` bash
python list.py [-h] [-t] [-p] [-v] [-d DEPTH] path

positional arguments:
  path                  path to list in

optional arguments:
  -h, --help            show this help message and exit
  -t, --tags            whether to print tags
  -p, --plain           plain text mode, effects disabled (colors, bold)
  -v, --validate        if filename matches tags, paints it green
  -d DEPTH, --depth DEPTH
                        restricts level of subfolders

```
e.g. `python list.py -t -v ~/Music/` prints something like:
![screenshot](https://raw.githubusercontent.com/markhovskiy/markhovskiy.github.io/master/uploads/music_cluster_screenshot.png)


### features/todo

- [x] print tree view of a folder (restrict depth, order subfiles by name)
- [x] use colors for file types
- [x] print tags table
- [x] validate file name against tags (`"<track number> - <title>.mp3"`)
- [ ] print last.fm metadata (e.g. http://www.last.fm/api/show/album.getInfo)
- [ ] introduce file-based configs for patterns, colors etc.
- [ ] add renaming capabilities (by patterns)
- [ ] add search capabilities


### links

* http://mutagen.readthedocs.org/en/latest/api/id3.html
