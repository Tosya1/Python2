
# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

# Задача для тестирования:
# Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную
# защищённую функцию.


import doctest
import unittest
import pytest


def check_date(date: str) -> bool:
    """
    >>> check_date('fgfhgfh')
    False

    >>> check_date(12583)
    Traceback (most recent call last):
    ...
    TypeError: Значение даты должно быть передано в виде строки формата "DD.MM.YYYY"

    >>> check_date('25.25.2000')
    False

    >>> check_date('29.02.1999')
    False

    >>> check_date('28.02.2020')
    True

    """
    if not isinstance(date, str):
        raise TypeError(
            'Значение даты должно быть передано в виде строки формата "DD.MM.YYYY"')
    try:
        day, month, year = [int(i) for i in date.split('.')]
        if day not in range(1, 32) or month not in range(1, 13) or year not in range(1, 10000):
            return False
        elif day == 31 and month in [4, 6, 9, 11]:
            return False
        elif _check_leap_year(year) and month == 2 and day in [30, 31] or \
                not _check_leap_year(year) and month == 2 and day in [29, 30, 31]:
            return False
        return True
    except:
        return False


def _check_leap_year(year: int) -> bool:
    if year % 4 or not year % 100 and year % 400:
        return False
    return True


class TestCheckDate(unittest.TestCase):

    def test_input_date_format(self):
        self.assertFalse(check_date('fgfhgfh'))

    def test_arg_type(self):
        with self.assertRaises(TypeError):
            check_date(12583)

    def test_non_existent_date(self):
        self.assertFalse(check_date('25.25.2000'))

    def test_leap_year(self):
        self.assertTrue(check_date('29.02.2020'))

    def test_correct_value(self):
        self.assertTrue(check_date('15.03.1985'))


def test_input_date_format():
    assert not check_date('fgfhgfh')


def test_arg_type():
    with pytest.raises(TypeError):
        check_date(12583)


def test_non_existent_date():
    assert not check_date('25.25.2000')


def test_leap_year():
    assert check_date('29.02.2020')


def test_correct_value():
    assert check_date('15.03.1985')


if __name__ == '__main__':
    doctest.testmod(verbose=2)
    unittest.main(verbosity=True)
    pytest.main(['-v'])
