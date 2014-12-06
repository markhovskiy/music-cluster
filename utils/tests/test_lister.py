# -*- coding: utf-8 -*-
from utils.lister import Lister


def test_max_tags_width():
    files = [
        {
            'name': '01 - The Moor.mp3',
            'ext': 'mp3',
            'tags': {
                'TPE1': 'Opeth',
                'TDRC': '1999',
                'TALB': 'Still Life',
                'TCON': 'Progressive Metal',
                'TRCK': '1',
                'TIT2': 'The Moor',
                'duration': '11:24'
            }
        },
        {
            'name': '10 - From So Far Away.mp3',
            'ext': 'mp3',
            'tags': {
                'TPE1': 'All Shall Perish',
                'TDRC': '2008',
                'TALB': 'Awaken the Dreamers',
                'TCON': 'Deathcore',
                'TRCK': '10',
                'TIT2': 'From So Far Away',
                'duration': '2:38'
            }
        },
        {
            'name': '11 - Дзеці паўночнага ветру.mp3',
            'ext': 'mp3',
            'tags': {
                'TPE1': 'Rokash',
                'TDRC': '2011',
                'TALB': u'Запалі Агонь',
                'TCON': 'Folk',
                'TRCK': '11',
                'TIT2': u'Дзеці паўночнага ветру',
                'duration': '5:11'
            }
        }
    ]

    assert Lister.max_tags_width(files) == {
        'TPE1': 16,
        'TDRC': 4,
        'TALB': 19,
        'TCON': 17,
        'TRCK': 2,
        'TIT2': 22,
        'duration': 5
    }


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
