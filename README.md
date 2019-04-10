# music-cluster

  [![license][license-image]][license-url]
  [![travis][travis-image]][travis-url]
  ![code size][code-size-image]

a CLI utility for dealing with local music collections

### setup (dev)

Install the [`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) and create a virtualenv for python2.7 (because `mutagen` can't really parse tags on python3).

```bash
$ pip install virtualenvwrapper
$ mkvirtualenv --python=/usr/bin/python2.7 music-cluster
$ workon music-cluster
$ pip install -r requirements.txt
```

### testing

```bash
$ py.test utils/tests/
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
![screenshot](/screenshot.png)

### features/todo

- [x] print tree view of a folder (restrict depth, order subfiles by name)
- [x] use colors for file types
- [x] print tags table
- [x] validate file name against tags (`"<track number> - <title>.mp3"`)
- [ ] migrate to python3
- [ ] add search capabilities

### links

* http://mutagen.readthedocs.org/en/latest/api/id3.html

[license-image]: https://img.shields.io/github/license/oleksmarkh/music-cluster.svg?style=flat-square
[license-url]: https://github.com/oleksmarkh/music-cluster/blob/master/LICENSE
[travis-image]: https://img.shields.io/travis/oleksmarkh/music-cluster/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/oleksmarkh/music-cluster
[code-size-image]: https://img.shields.io/github/languages/code-size/oleksmarkh/music-cluster.svg?style=flat-square
