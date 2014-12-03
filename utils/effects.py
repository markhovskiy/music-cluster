# see http://en.wikipedia.org/wiki/ANSI_escape_code#Colors
codes = {
    'reset': 0,
    'bold': 1,
    'grey': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
}


def escape(*effect):
    return "\x1b[{}m".format(';'.join([str(codes.get(e, 0)) for e in effect]))


def apply(text, *effect):
    return u"{start}{text}{end}".format(start=escape(*effect),
                                        text=text,
                                        end=escape('reset'))


def get_ext_color(ext):
    return dict(mp3='blue',
                jpg='yellow',
                jpeg='yellow').get(ext, 'grey')
