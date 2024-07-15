from solution import get_median_value


def test__get_median_value__1():
    list_example = [20, 11.9, 30.20, 11.8]
    assert get_median_value(list_example) == 11.9


def test__get_median_value__2():
    list_example = [20, 11.9, 30.20, 11.9]
    assert get_median_value(list_example) == 11.9


def test__get_median_value__3():
    list_example = [20, 1.9, 30.20, 2.9, 0.0]
    assert get_median_value(list_example) == 2.9


def test__get_median_value__4():
    list_example = [20.0]
    assert get_median_value(list_example) == 20.0
