# 1.Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import random
import time


class MyString(str):
    """Расширяемый класс str."""
    def __new__(cls, value: str, autor: str):
        """Метод расширяет класс параметрами:
        Args:
            value (str): передаваемое значение
            autor (str): имя автора строки
        """
        instance = super().__new__(cls, value)
        instance.autor = autor
        instance.time = time.time()
        return instance

    def __str__(self) -> str:
        """Функция создает представление для пользователя экземпляра класса."""
        return f'{super().__str__()}, Автор: {self.autor}, Время создания: {self.time}'

    def __repr__(self) -> str:
        """Функция возвращает представление для создания экземпляра класса."""
        return f'MyString({super().__repr__()}, \'{self.autor}\')'

# 2.Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


class Archive:
    """Класс хранит данные экземпляров классов в списках numbers и strings."""

    numbers = []
    strings = []

    def __new__(cls, number: int, string: str):
        """Метод расширяет класс параметрами:
        Args:
            number (int): произвольное число
            string (str): произвольная строка
        """
        instance = super().__new__(cls)
        instance.numbers.append(number)
        instance.strings.append(string)
        return instance

    def __init__(self, number: int, string: str):
        """Метод инициализации экземпляра класса.
        Args:
            number (int): произвольное число
            string (str): произвольная строка
        """
        self.number = number
        self.string = string

    def __str__(self) -> str:
        """Функция создает представление для пользователя экземпляра класса."""
        return f'Номер: {self.number} Строка: {self.string}'

    def __repr__(self) -> str:
        """Функция возвращает представление для создания экземпляра класса."""
        return f'Archive({self.number}, \'{self.string}\')'


# 3.Добавьте к задачам 1 и 2 строки документации для классов.

# 4Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

# 5.Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# 6.Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """Класс для работы с прямоугольниками"""

    def __init__(self, length: int, width: int = None):
        """Метод инициализации экземпляра класса.
        Args:
            length (int):длина прямоугольника
            width (int, optional): ширина прямоугольника.
            Значение по умолчанию -  None.
        """
        self.length = length
        self.width = width if width is not None else length

    def get_perimeter(self) -> int:
        """Функция нахождения периметра прямоугольника.
        Returns:
            int: периметр прямоугольника
        """
        return 2 * (self.length + self.width)

    def get_area(self) -> int:
        """Функция нахождения площади прямоугольника.
        Returns:
            int: площадь прямоугольника
        """
        return self.length * self.width

    def __add__(self, other: object):
        """Функция сложения 2 прямоугольников (периметров).
        Args:
            other (Rectangle): прямоугольник, с которым
            производится операция сложение текущего экземпляра класса
        Returns:
            Rectangle: новый экземпляр класса Rectangle
        """
        perimeter = self.get_perimeter() + other.get_perimeter()
        length = random.randint(1, perimeter/2 - 1)
        new_rect = Rectangle(length, int(perimeter/2 - length))
        return new_rect

    def __sub__(self, other: object):
        """Функция вычитания 2 прямоугольников (периметров).
        Args:
            other (Rectangle): прямоугольник, с которым
            производится операция вычитания из текущего экземпляра класса
        Returns:
            Rectangle: новый экземпляр класса Rectangle
        """
        perimeter = abs(self.get_perimeter() - other.get_perimeter())
        if perimeter > 2:
            length = random.randint(1, perimeter/2 - 1)
            new_rect = Rectangle(length, int(perimeter/2 - length))
            return new_rect
        else:
            return Rectangle(None, None)

    def __eq__(self, other: object) -> bool:
        """Метод сравнения 2 прямоугольников по их площади
        Args:
            other (Rectangle): прямоугольник, с которым
            производится сравнение текущего экземпляра класса
        Returns:
            bool: True, если площади прямоугольников равны,
            False, если площади прямоугольников не равны
        """
        return self.get_area() == other.get_area()

    def __gt__(self, other: object) -> bool:
        """Метод проверяет больше ли текущий экземпляр класса второго
        переданного прямоугольника по площади.
        Args:
            other (Rectangle): прямоугольник, с которым
            производится сравнение текущего экземпляра класса
        Returns:
            bool: True, если площади прямоугольников равны,
            False, если площади прямоугольников не равны
        """
        return self.get_area() > other.get_area()

    def __ge__(self, other: object) -> bool:
        """Метод провеяет больше или равен текущий экземпляр класса относительно 
        второго переданного прямоугольника по площади.
        Args:
            other (Rectangle): прямоугольник, с которым
            производится сравнение текущего экземпляра класса
        Returns:
            bool: True, если площади прямоугольников равны,
            False, если площади прямоугольников не равны
        """
        return self.get_area() >= other.get_area()

    def __str__(self) -> str:
        """Функция создает представление для пользователя экземпляра класса."""
        return f'Длина: {self.length}, Ширина: {self.width}'

    def __repr__(self) -> str:
        return f'Rectangle({self.length}, {self.width})'


if __name__ == '__main__':
    str1 = MyString('Строка', 'autor1')
    str2 = MyString('Строка2', 'autor2')
    print(str1, str2, sep='\n')
    print(f'{str1=}')
    a1 = Archive(1, 'One')
    print(f'{a1} {a1=}')
    a2 = Archive(2, 'Two')
    print(f'{a2} {a2=}')
    rect1 = Rectangle(5, 6)
    rect2 = Rectangle(6, 2)
    rect3 = rect1 + rect2
    rect4 = rect1 - rect2
    print(f'rect1 = {rect1}, Периметр: {rect1.get_perimeter()}, Площадь: {rect1.get_area()}')
    print(f'rect2 = {rect2}, Периметр: {rect2.get_perimeter()}, Площадь: {rect2.get_area()}')
    print(f'rect3 = {rect3}, Периметр: {rect3.get_perimeter()}, Площадь: {rect3.get_area()}')
    print(f'rect4 = {rect4}, Периметр: {rect4.get_perimeter()}, Площадь: {rect4.get_area()}')
    print(f'{rect1=}')
    print(f'{rect1 >= rect2=}')
    print(f'{rect1 <= rect2=}')
    print(f'{rect3 == rect2=}')
    print(f'{rect1 != rect2=}')
    print(f'{rect3 >= rect2=}')
    print(f'{rect3 >= rect4=}')
