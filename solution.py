from typing import Optional
from datetime import datetime


# Zadanie

# Wyznacz medianę wydatków do pierwszej niedzieli (włącznie) każdego miesiąca
# (np. dla 2023-09 i 2023-10 są to dni 1, 2, 3 wrz i 1 paź).


# Analiza zadania:
#  - mają być brane pod uwagę tylko wydatki do pierwszej niedzieli każdego miesiąca
#  - mają zostać przeanalizowane dane dla miesięcy (od 0 do n)
#     ---> policzyć sumy wydatków dla każdego miesiąca (do pierwszej niedzieli)
#  - dla policzonych sum wyznaczyć medianę


expenses = {
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


#
def get_first_sunday(year: int, month: int) -> int:
    """ Deducts number related to first sunday of the week.

    Args:
        year (int): year number,
        month (int): month number

    Returns:
        Number of first sunday of the month
    """

    day_ = 1

    while True:
        month_datetime = datetime(year=year, month=month, day=day_)
        if month_datetime.weekday() == 6:
            return day_
        day_ += 1


def get_median_value(data: list[float]) -> float:
    """ Deducts median value for list of float numbers

    Args:
        data (list[float]): list of float numbers
                            Examples:
                                [20, 11.9, 30.20, 11.8]
                                [20, 11.9, 30.20, 11.8, 0.0]

    Returns:
        Median value for list of float numbers
                                11.9 - [20, 11.9, 30.20, 11.8]
                                11.9 - [20, 11.9, 30.20, 11.8, 0.0]
    """
    data.sort()
    data_len = len(data)

    if bool(data_len % 2):
        # number of elements in list is odd
        # then median is simply middle value in ordered list
        median_index = data_len // 2
        return data[median_index]
    else:
        # number of elements in list is even
        # then median is "first-left-middle" value in ordered list
        median_index = data_len // 2 - 1
        return data[median_index]


class ExpensesMonthConverter:
    """ Converter providing api for monthly expenses.

    Args:
        year (int): year number,
        month (int): month number
        expenses_month (dict): data structure containing expenses for the given month

    Attributes:
        __year (int): year number,
        __month (int): month number
        __expenses_month (dict): data structure containing expenses for the given month
                              example:
                                {
                                    "01": {
                                        "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
                                        "fuel": [210.22]
                                    },
                                    "09": {
                                        "food": [11.9],
                                        "fuel": [190.22]
                                    }
                                }
    """

    def __init__(self, year: int, month: int, expenses_month: dict):
        self.__year = year
        self.__month = month
        self.__expenses_month = expenses_month

    def calculate_first_week_expenses_sum(self) -> float:
        """ Method calcs month expenses considering only first week data samples.

        Returns:
            Sum of the expenses for the given month considering only first week data samples.
        """
        expenses_data = self.get_first_week_data_only()

        first_week_expenses_sum = 0
        for day_, data_ in expenses_data.items():
            for data_value in data_.values():
                first_week_expenses_sum += sum(data_value)

        return float(first_week_expenses_sum)

    def get_first_week_data_only(self):
        """ Method filters out month expenses data to have only first week data samples.

         Example:
             When self.__expenses_month is
                                 {
                                    "01": {
                                        "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
                                        "fuel": [210.22]
                                    },
                                    "09": {
                                        "food": [11.9],
                                        "fuel": [190.22]
                                    }
                                }

            then it returns:
                                {
                                    "01": {
                                        "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
                                        "fuel": [210.22]
                                    }
                                }
        """
        first_sunday = get_first_sunday(year=self.__year, month=self.__month)

        filtered_data = {}

        for day_, data_ in self.__expenses_month.items():
            if int(day_) <= first_sunday:
                filtered_data[day_] = data_

        return filtered_data


def solution(expenses_struct: dict) -> Optional[float]:
    """ Solves assignment problem """
    expenses = []
    for month_str, month_data in expenses_struct.items():
        year = int(month_str[0:4])
        month = int(month_str[5:])
        expense_month_converter = ExpensesMonthConverter(year=year, month=month, expenses_month=month_data)
        expense_month_sum = expense_month_converter.calculate_first_week_expenses_sum()

        expenses.append(expense_month_sum)

    if not expenses:
        return None

    median_value = get_median_value(expenses)
    return median_value


print(solution(expenses))
