from solution import solution

expenses_example1 = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}



expenses_example2 = {
    "2023-01": {
        "01": {
            "food": [1.72, 2.2],
        },
        "09": {
            "food": [11.9],
            "fuel": [1.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}


def test__solution__1():
    assert solution(expenses_example1) == 24.2


def test__solution__2():
    assert solution(expenses_example2) == 3.92


def test__solution__3():
    assert solution({}) is None

