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
e.g. `python list.py -c -t -d 3 -p ~/Music/` will print something like:
```
Обiйми дощу
  2010 - Свiтанок
    folder.jpg
    Обiйми дощу | 2010 | Обiйми дощу | Progressive Rock | 2 | Світанок | 02-obiymy_doschu-svitanok.mp3
    Обiйми дощу | 2010 | Обiйми дощу | Progressive Rock | 1 | Я і Ти   | 01-obiymy_doschu-ya_i_ty.mp3
  2009 - Елегiя
    folder.jpg
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 6 | Зимова Елегія         | 06-obiymy_doschu-zymova_elehia.mp3
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 7 | Самотні Ночі          | 07-obiymy_doschu-samotni_nochi.mp3
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 2 | Мертве Дерево і Вітер | 02-obiymy_doschu-mertve_derevo_i_viter.mp3
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 8 | Дорогою Вічності      | 08-obiymy_doschu-dorohoyu_vichnosti.mp3
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 4 | Її Душі Зів'ялі Квіти | 04-obiymy_doschu-yiyi_dushi_zivyali_kvity.mp3
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 5 | Згасаюча Осінь        | 05-obiymy_doschu-zhasayucha_osin.mp3
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 3 | Зоренько Моя          | 03-obiymy_doschu-zorenko_moya.mp3
    Обiйми дощу | 2009 | Обiйми дощу | Progressive Rock | 1 | Під Хмарами           | 01-obiymy_doschu-pid_hmaramy.mp3
Рокаш
  2011 - Запалі Агонь
    Rokash | 2011 | Запалі Агонь | Folk | 02 | Крумкач                        | 02. Крумкач.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 12 | Балада пра ліцьвіна (акустыка) | 12. Балада пра ліцьвіна (акустыка).mp3
    Rokash | 2011 | Запалі Агонь | Folk | 01 | Запалі агонь                   | 01. Запалі агонь.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 07 | Крылы                          | 07. Крылы.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 13 | Зялёныя рукавы (акустыка)      | 13. Зялёныя рукавы (акустыка).mp3
    Rokash | 2011 | Запалі Агонь | Folk | 11 | Дзеці паўночнага ветру         | 11. Дзеці паўночнага ветру.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 10 | У лясным гушчары               | 10. У лясным гушчары.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 09 | У тваіх вачах                  | 09. У тваіх вачах.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 04 | Сокал                          | 04. Сокал.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 06 | Хмяльны Бранль                 | 06. Хмяльны Бранль.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 05 | Духі Зямлі                     | 05. Духі Зямлі.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 08 | Ваўкалак                       | 08. Ваўкалак.mp3
    Rokash | 2011 | Запалі Агонь | Folk | 03 | Восень                         | 03. Восень.mp3
Between the Buried and Me | 2006 | Alaska | Metal | 2 | Alaska | 4:58 | Alaska.mp3
```

### todo

* order by file name
* add functionality for checking a file tree against tags (e.g. `"<artist>" -> "<year> - <album>" -> "<track number> - <title>.mp3"`)
* introduce file-based configs for patterns, colors etc.
* add renaming capabilities (by patterns)
* add search capabilities
* take advantage of last.fm stats (e.g. http://www.last.fm/api/show/track.getTags)

### links

* http://mutagen.readthedocs.org/en/latest/api/id3.html
