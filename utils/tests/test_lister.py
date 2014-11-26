from utils.lister import Lister


def test_format_duration():
    assert Lister.format_duration(12.3812) == "0:12"
    assert Lister.format_duration(185.4432) == "3:05"
    assert Lister.format_duration(212.6367) == "3:32"
    assert Lister.format_duration(212.6367) == "3:32"
