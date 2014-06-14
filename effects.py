effect_codes = {
  'end': '\033[0m',
  'bold': '\033[1m',
  'colors': {
    'grey': '\033[90m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
  }
}

ext_colors = {
  'mp3': 'blue',
  'jpg': 'yellow',
  'jpeg': 'yellow',
}

def get_ext_color(ext):
  return effect_codes['colors'][ext_colors.get(ext, 'grey')]
