from solution import get_first_sunday, ExpensesMonthConverter


expense_2023_01 = {
    "01": {
        "food": [22.11, 43],
        "fuel": [210.22]
    },
    "09": {
        "food": [22.11, 43],
        "fuel": [190.22]
    }
}

first_sunday_expense_2023_01 = {
    "01": {
        "food": [22.11, 43],
        "fuel": [210.22]
    }
}



def test__ExpensesMonthConverter_init():
    assert ExpensesMonthConverter(year=2023, month=1, expenses_month=expense_2023_01)


def test__ExpensesMonthConverter__first_sunday_data():
    first_sunday_data = ExpensesMonthConverter(year=2023, month=1, expenses_month=expense_2023_01)

    assert first_sunday_data.get_first_week_data_only() == first_sunday_expense_2023_01


def test__ExpensesMonthConverter__first_sunday_data__calculate_first_week_expenses_sum():
    first_sunday_data = ExpensesMonthConverter(year=2023, month=1, expenses_month=expense_2023_01)

    assert first_sunday_data.calculate_first_week_expenses_sum() == 275.33


def test__ExpensesMonthConverter__first_sunday__empty_expenses():
    first_sunday_data = ExpensesMonthConverter(year=2023, month=1, expenses_month={})

    assert first_sunday_data.get_first_week_data_only() == {}


def test__ExpensesMonthConverter__first_sunday_data__calculate_first_week_expenses_sum__empty_expenses():
    first_sunday_data = ExpensesMonthConverter(year=2023, month=1, expenses_month={})

    assert first_sunday_data.calculate_first_week_expenses_sum() == 0.0
