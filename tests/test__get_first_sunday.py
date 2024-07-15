from solution import get_first_sunday


def test__get_first_sunday__2024_07():
    day_ = get_first_sunday(year=2024, month=7)
    assert day_ == 7


def test__get_first_sunday__2024_06():
    day_ = get_first_sunday(year=2024, month=6)
    assert day_ == 2


def test__get_first_sunday__2024_05():
    day_ = get_first_sunday(year=2024, month=5)
    assert day_ == 5


def test__get_first_sunday__2024_04():
    day_ = get_first_sunday(year=2024, month=4)
    assert day_ == 7


def test__get_first_sunday__2024_03():
    day_ = get_first_sunday(year=2024, month=3)
    assert day_ == 3


def test__get_first_sunday__2024_02():
    day_ = get_first_sunday(year=2024, month=2)
    assert day_ == 4


def test__get_first_sunday__2024_01():
    day_ = get_first_sunday(year=2024, month=1)
    assert day_ == 7


def test__get_first_sunday__2023_12():
    day_ = get_first_sunday(year=2023, month=12)
    assert day_ == 3


def test__get_first_sunday__2023_11():
    day_ = get_first_sunday(year=2023, month=11)
    assert day_ == 5


def test__get_first_sunday__2023_10():
    day_ = get_first_sunday(year=2023, month=10)
    assert day_ == 1


def test__get_first_sunday__2023_09():
    day_ = get_first_sunday(year=2023, month=9)
    assert day_ == 3
