# see http://en.wikipedia.org/wiki/ANSI_escape_code#Colors
effect_codes = {
    'end': '\033[0m',
    'bold': '\033[1m',
    'colors': {
        'grey': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
    }
}


def wrap(text, effect):
    effect_code = effect_codes['colors'].get(effect,
                                             effect_codes.get(effect, ''))
    return "{start}{text}{end}".format(start=effect_code,
                                       text=text,
                                       end=effect_codes['end'])


def get_ext_color(ext):
    return dict(mp3='blue',
                jpg='yellow',
                jpeg='yellow').get(ext, 'grey')
