# 1.Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
import logging
import random
import argparse


class Matrix:
    MIN_VALUE = 0
    MAX_VALUE = 10

    def __init__(self, rows_count: int, columns_count: int):
        self.rows_count = rows_count
        self.columns_count = columns_count
        self.matrix = [[random.randint(self.MIN_VALUE, self.MAX_VALUE) for _ in range(
            self.columns_count)] for _ in range(self.rows_count)]
        self.logger().info(f'создана матрица {self.matrix}')

    def __str__(self) -> str:
        return '\n'.join([' '.join(list(map(str, i))) for i in self.matrix])

    def __eq__(self, other: object) -> bool:
        self.logger().info(
            f'проверка на равенство матриц {self.matrix} и {other.matrix}: {self.matrix == other.matrix}')
        return self.matrix == other.matrix

    def __add__(self, other: object):
        if self.rows_count == other.rows_count and self.columns_count == other.columns_count:
            matrix = [[i + j for i, j in zip(i, j)]
                      for i, j in zip(self.matrix, other.matrix)]
            res = Matrix(self.rows_count, self.columns_count)
            res.matrix = matrix
            self.logger().info(
                f'выполнена операция сложения матриц {self.matrix} и {other.matrix}.\nРезультирующая матрица : {res.matrix}')
            return res
        else:
            self.logger().error(
                'невозможно выполнить операцию сложения: количество столбцов и строк в матрицах не совпадают!')
            raise ValueError(
                'Количество столбцов и строк в матрицах должно совпадать!')

    def __mul__(self, other: object):
        if self.columns_count == other.rows_count:
            matrix = [[sum(i * j for i, j in zip(i, j))
                       for j in zip(*other.matrix)] for i in self.matrix]
            res = Matrix(self.rows_count, other.columns_count)
            res.matrix = matrix
            self.logger().info(
                f'выполнена операция умножения матриц {self.matrix} и {other.matrix}.\nРезультирующая матрица : {res.matrix}')
            return res
        else:
            self.logger().error('невозможно выполнить операцию умножения: количество столбцов в первой матрице и количество строк во второй матрице не совпадают!')
            raise ValueError(
                'Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице!')

    def logger(self):
        FORMAT = '{levelname:<8} - {asctime}: {msg}'
        logging.basicConfig(filename=f'{self.__class__.__name__}.log', filemode='w',
                            encoding='utf-8', format=FORMAT, style='{', level=logging.INFO)
        return logging.getLogger(__name__)

    def parser():
        parser = argparse.ArgumentParser(description='Parser for Matrix')
        parser.add_argument('numbers', metavar='N', type=int, nargs=2,
                            help='Enter the number of rows and columns of the matrix')
        return Matrix(*parser.parse_args().numbers)


if __name__ == '__main__':
    m1 = Matrix(3, 2)
    m2 = Matrix(3, 2)
    print(f'm1:\n{m1}\n')
    print(f'm2:\n{m2}\n')
    print(f'm1 + m2:\n{m1 + m2}\n')
    print(f'm1 = m2:\n{m1 == m2}\n')
    m3 = Matrix(2, 4)
    print(f'm3:\n{m3}\n')
    m4 = m1 * m3
    print(f'm4:\n{m4}')
    m5 = Matrix.parser()  # ввести значения в командной строке
    print(f'm5:\n{m5}')
    print(m1 + m3)
