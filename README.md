# music-cluster

  [![license][license-image]][license-url]
  ![code size][code-size-image]

A CLI utility for dealing with local music collections.
It aims to keep `*.mp3` files organized, providing read-only capabilities.
For altering tags, more powerful tools could be used, e.g. [MusicBrainz Picard](https://picard.musicbrainz.org/).

## Status
*In progress* - you can use it, but it's not distributed as a package yet.

## How does it look like?
![screenshot](/screenshot.png)

## How to run it?
```bash
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

For example:
```bash
$ python list.py -t -v ~/Music/
```

## What makes it possible?
### dev deps
* [`virtualenv`](https://virtualenv.pypa.io/) - environment isolation scripts
* [`pycodestyle`](https://pycodestyle.readthedocs.io/) - a codestyle checker
* [`pytest`](https://pytest.org/) - unit testing framework

### deps
* [Mutagen](https://mutagen.readthedocs.io/) - a tagging library

## Development setup
Create a [virtual Python 3.7 environment](https://virtualenv.pypa.io/), since Mutagen is dependent on Python 3.7.

```bash
# virtual environment
$ pip3 install virtualenv
$ virtualenv --python=python3.7 music-cluster-env
$ source ./music-cluster-env/bin/activate

# dependencies
$ pip install -r ./requirements.txt

# codestyle
$ pycodestyle --show-source ./list.py ./utils/

# unit tests
$ py.test ./utils/tests/
```

## Invitation for contributors
PRs and bug reports are very welcome.

[license-image]: https://img.shields.io/github/license/oleksmarkh/music-cluster.svg?style=flat-square
[license-url]: https://github.com/oleksmarkh/music-cluster/blob/master/LICENSE
[code-size-image]: https://img.shields.io/github/languages/code-size/oleksmarkh/music-cluster.svg?style=flat-square
