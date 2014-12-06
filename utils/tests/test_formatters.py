from utils.formatters import to_time_str


def test_to_time_str():
    assert to_time_str(0) == "0:00"
    assert to_time_str(2.6123) == "0:02"
    assert to_time_str(12.3812) == "0:12"
    assert to_time_str(3*60 + 5.4432) == "3:05"
    assert to_time_str(3*60 + 32.6367) == "3:32"
    assert to_time_str(20*60 + 59.7654) == "20:59"
    assert to_time_str(1*3600 + 1*60 + 9.2346) == "1:01:09"
