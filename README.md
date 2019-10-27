# music-cluster

  [![license][license-image]][license-url]
  [![travis][travis-image]][travis-url]
  ![code size][code-size-image]

a CLI utility for dealing with local music collections

### setup (dev)

Install a [`virtual Python 3.7 environment`](https://virtualenv.pypa.io/en/latest/installation/) 
and create a virtualenv for Python 3.7 (because one of the primary
dependencies in requirements.txt, `mutagen` is dependent on Python 3.7).

```bash
$ cd music-cluster
$ pip3 install virtualenv
$ virtualenv --python=python3.7 music-cluster-env
$ source music-cluster-env/bin/activate
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
- [x] migrate to python3
- [ ] add search capabilities

### links

* http://mutagen.readthedocs.org/en/latest/api/id3.html

[license-image]: https://img.shields.io/github/license/oleksmarkh/music-cluster.svg?style=flat-square
[license-url]: https://github.com/oleksmarkh/music-cluster/blob/master/LICENSE
[travis-image]: https://img.shields.io/travis/oleksmarkh/music-cluster/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/oleksmarkh/music-cluster
[code-size-image]: https://img.shields.io/github/languages/code-size/oleksmarkh/music-cluster.svg?style=flat-square
