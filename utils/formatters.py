import math


def to_time_str(s_float):
    """
    Formats given number of seconds (float) as "h:m:s"

    "h:" part appears only if h>0
    "m" are aligned with leading 0 only if h>0
    "s" are always aligned with leading 0
    """

    h = math.floor(s_float / 3600)
    m = math.floor((s_float - h * 3600) / 60)
    s = math.floor(s_float % 60)

    return "{}{}:{}".format("{:.0f}:".format(h) if h else '',
                            "{:0>{}.0f}".format(m,
                                                2 if h else 1),
                            "{:0>2.0f}".format(s))
