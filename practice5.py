# 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

path = "C:\\Users\\tosya\\Documents\\Python\\practice5.py"


def get_path_tuple(path_str: str) -> tuple[str]:
    temp, ext = path_str.split('.')
    *file_path, name = temp.split('\\')
    file_path = '\\'.join(file_path)
    return (file_path, name, ext)


print(get_path_tuple(path), sep=',')

# 2. Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Петя', 'Вася', 'Коля']
rates = [20000, 50000, 100000]
bonus_pers = ['10.25%', '5.75%', '2.5%']

print(*({i: int(j * float(k.replace('%', ''))/100)}
      for i, j, k in zip(names, rates, bonus_pers)))

# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def fibonacci_gen(n: int):
    fib1 = fib2 = 1
    for i in range(1, n + 1):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


print(*fibonacci_gen(10))
