# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
import random


class Matrix:
    """Класс для создания и осуществления арифметических операций с матрицами"""
    MIN_VALUE = 0
    MAX_VALUE = 10

    def __init__(self, rows_count: int, columns_count: int):
        """Инициализация экземпляра класса

        Args:
            rows_count (int): количество рядов матрицы
            columns_count (int): количество столбцов матрицы
        """
        self.rows_count = rows_count
        self.columns_count = columns_count
        self.matrix = [[random.randint(self.MIN_VALUE, self.MAX_VALUE) for _ in range(
            self.columns_count)] for _ in range(self.rows_count)]

    def __str__(self) -> str:
        """Функция представления для пользователя экземпляра класса
        Returns:
            str: параметр matrix экземпляра класса в строковом представлении
        """
        return '\n'.join([' '.join(list(map(str, i))) for i in self.matrix])

    def __eq__(self, other: object) -> bool:
        """Функция проверки равенства двух матриц
        Args:
            other (object): матрица, с которой сравниваем текущий экземпляр класса
        Returns:
            bool: True, если матрицы равны, и False, если матрицы не равны
        """
        return self.matrix == other.matrix

    def __add__(self, other: object):
        """Функция сложения двух матриц
        Args:
            other (Matrix): матрица, с которой производим операцию сложения
            текущего экземпляра класса
        Returns:
            Matrix: новый экземпляр класса
            None: в случае ошибки аргументов при операции сложения
        """
        if self.rows_count == other.rows_count and self.columns_count == other.columns_count:
            matrix = [[i + j for i, j in zip(i, j)]
                      for i, j in zip(self.matrix, other.matrix)]
            res = Matrix(self.rows_count, self.columns_count)
            res.matrix = matrix
            return res
        else:
            print('Количество столбцов и строк в матрицах должно совпадать!')
            return None

    def __mul__(self, other: object):
        """Функция умножения двух матриц
        Args:
            other (object): матрица, с которой производим операцию умножения
            текущего экземпляра класса
        Returns:
            Matrix: новый экземпляр класса
            None: в случае ошибки аргументов при операции умножения
        """
        if self.columns_count == other.rows_count:
            matrix = [[sum(i * j for i, j in zip(i, j))
                       for j in zip(*other.matrix)] for i in self.matrix]
            res = Matrix(self.rows_count, other.columns_count)
            res.matrix = matrix
            return res
        else:
            print(
                f'Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице!')
            return None


if __name__ == '__main__':

    m1 = Matrix(3, 2)
    m2 = Matrix(3, 2)
    print(f'm1:\n{m1}\n')
    print(f'm2:\n{m2}\n')
    print(f'm1 + m2:\n{m1 + m2}\n')
    m3 = Matrix(2, 4)
    print(f'm3:\n{m3}\n')
    m4 = m1 * m3
    print(f'm4:\n{m4}')
    help(Matrix)
