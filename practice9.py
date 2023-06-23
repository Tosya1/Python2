# 1.Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random

MIN_COUNT = 100
MAX_COUNT = 1000
MIN_COEFFICIENT = -200
MAX_COEFFICIENT = 200


def create_num_file(file):
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(random.randint(MIN_COUNT, MAX_COUNT + 1)):
            a = random.randint(MIN_COEFFICIENT, MAX_COEFFICIENT)
            if a != 0:
                writer.writerow([a, random.randint(MIN_COEFFICIENT, MAX_COEFFICIENT),
                                random.randint(MIN_COEFFICIENT, MAX_COEFFICIENT)])


def solve_from_csv(file):
    def deco_func(func):
        create_num_file(file)

        def wrapper():
            with open(file, 'r', newline='') as f:
                reader = csv.reader(f, dialect='excel',
                                    quoting=csv.QUOTE_NONNUMERIC)
                for line in reader:
                    func(*line)
        return wrapper
    return deco_func


def write_to_json(file):
    def deco_func(func):
        res = []

        def wrapper(*args):
            with open(file, 'w', encoding='utf-8') as f:
                res.append({'a': args[0], 'b': args[1],
                           'c': args[2], 'roots': func(*args)})
                json.dump(res, f, ensure_ascii=False, indent=2)
            return func(*args)
        return wrapper
    return deco_func


@solve_from_csv('nums.csv')
@write_to_json('solutions.json')
def get_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = round((-b - d ** 0.5) / (2 * a), 2)
        x2 = round((-b + d ** 0.5) / (2 * a), 2)
    else:
        # x1 = (-b - complex(d) ** 0.5)/ (2 * a)
        # x2 = (-b + complex(d) ** 0.5)/ (2 * a)
        x1 = x2 = None
    return x1, x2


get_roots()
