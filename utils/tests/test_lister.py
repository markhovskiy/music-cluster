# -*- coding: utf-8 -*-
from utils.lister import FileData, Lister


def test_has_valid_name():
    file_data_wrong = FileData('something.mp3')
    file_data_wrong.tags = dict(TRCK='01',
                                TIT2='another thing')
    assert not file_data_wrong.has_valid_name()

    file_data_correct = FileData('02 - Alaska.mp3')
    file_data_correct.tags = dict(TRCK='02',
                                  TIT2='Alaska')
    assert file_data_correct.has_valid_name()


def test_max_tags_length():
    file_data_0 = FileData('01 - The Moor.mp3')
    file_data_0.tags = dict(TPE1='Opeth',
                            TDRC='1999',
                            TALB='Still Life',
                            TCON='Progressive Metal',
                            TRCK='1',
                            TIT2='The Moor',
                            duration='11:24')

    file_data_1 = FileData('10 - From So Far Away.mp3')
    file_data_1.tags = dict(TPE1='All Shall Perish',
                            TDRC='2008',
                            TALB='Awaken the Dreamers',
                            TCON='Deathcore',
                            TRCK='10',
                            TIT2='From So Far Away',
                            duration='2:38')

    file_data_2 = FileData('11 - Дзеці паўночнага ветру.mp3')
    file_data_2.tags = dict(TPE1='Rokash',
                            TDRC='2011',
                            TALB=u'Запалі Агонь',
                            TCON='Folk',
                            TRCK='11',
                            TIT2=u'Дзеці паўночнага ветру',
                            duration='5:11')

    files = [file_data_0, file_data_1, file_data_2]
    assert Lister.max_tags_length(files) == dict(TPE1=16,
                                                 TDRC=4,
                                                 TALB=19,
                                                 TCON=17,
                                                 TRCK=2,
                                                 TIT2=22,
                                                 duration=5)


def test_highlight():
    plain_lister = Lister(to_disable_effects=True)
    assert plain_lister.highlight("text", 'red') == "text"
    assert plain_lister.highlight(u" \u2758 ", 'red') == u" ❘ "

    colored_lister = Lister(to_disable_effects=False)
    assert colored_lister.highlight("text",
                                    'red') == "\x1b[31mtext\x1b[0m"
    assert colored_lister.highlight(u" \u2758 ",
                                    'red') == u"\x1b[31m ❘ \x1b[0m"
    assert colored_lister.highlight("text",
                                    'blue',
                                    'bold') == "\x1b[34;1mtext\x1b[0m"


def test_print_file_data(capsys):
    file_data = FileData('WLSTD.mp3')
    file_data.tags = dict(TPE1='HIM',
                          TDRC='2013',
                          TALB='ToT',
                          TCON='Rock',
                          TRCK='12',
                          TIT2='WLSTD',
                          duration='4:12')

    plain_lister = Lister(to_disable_effects=True)
    plain_lister.print_file_data(file_data, {})

    out, err = capsys.readouterr()
    assert out == u"HIM ❘ 2013 ❘ ToT ❘ Rock ❘ 12 ❘ WLSTD ❘ 4:12 ❘ WLSTD.mp3\n"
