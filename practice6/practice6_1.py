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

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from sys import argv


YEAR_LIMIT = range(1, 10000)
MONTH_LIMIT = range(1, 13)
DAY_LIMIT = range(1, 32)
SHORT_MONTHS = (4, 6, 9, 11)
LY_TEST1 = 4
LY_TEST2 = 100
FEB = 2
FEB_TEST1 = (30, 31)
FEB_TEST2 = range(29, 32)

# checks if the date exists


def check_date(date: str) -> bool:
    day, month, year = [int(i) for i in date.split('.')]
    if day not in DAY_LIMIT or month not in MONTH_LIMIT or year not in YEAR_LIMIT:
        return False
    elif day == 31 and month in SHORT_MONTHS:
        return False
    elif _check_leap_year(year) and month == FEB and day in FEB_TEST1 or \
            not _check_leap_year(year) and month == FEB and day in FEB_TEST2:
        return False
    return True

# checks if the year is a leap year


def _check_leap_year(year: int) -> bool:
    if year % LY_TEST1 or not year % LY_TEST2 and year % (LY_TEST1 * LY_TEST2):
        return False
    return True


print(check_date(argv[1]))
