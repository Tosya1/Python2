# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации. Поднимайте
# исключения внутри основного кода. Например нельзя создавать прямоугольник со
# сторонами отрицательной длины.

import random


class Rectangle:

    def __init__(self, length: int, width: int = None):
        self.length = Rectangle.check_value(length, 1, 'Длина')
        self.width = Rectangle.check_value(
            width, 1, 'Ширина') if width is not None else self.length

    def check_value(value: int, min_value: int, attr_name: str):
        if not isinstance(value, int):
            raise ValueError(f'{attr_name} {value} должна быть целым числом!')
        elif value >= min_value:
            return value
        else:
            raise RectValueException(attr_name, value, min_value)

    def get_perimeter(self) -> int:
        return 2 * (self.length + self.width)

    def get_area(self) -> int:
        return self.length * self.width

    def __add__(self, other: object):
        perimeter = self.get_perimeter() + other.get_perimeter()
        length = random.randint(1, perimeter/2 - 1)
        new_rect = Rectangle(length, int(perimeter/2 - length))
        return new_rect

    def __sub__(self, other: object):
        perimeter = abs(self.get_perimeter() - other.get_perimeter())
        if perimeter > 2:
            length = random.randint(1, perimeter/2 - 1)
            new_rect = Rectangle(length, int(perimeter/2 - length))
            return new_rect
        else:
            raise RectValueException('Периметр', perimeter, 2)
            return Rectangle(None, None)

    def __eq__(self, other: object) -> bool:
        return self.get_area() == other.get_area()

    def __gt__(self, other: object) -> bool:
        return self.get_area() > other.get_area()

    def __ge__(self, other: object) -> bool:
        return self.get_area() >= other.get_area()

    def __str__(self) -> str:
        return f'Длина: {self.length}, Ширина: {self.width}'

    def __repr__(self) -> str:
        return f'Rectangle({self.length}, {self.width})'


class RectValueException(Exception):
    def __init__(self, name: str, value: int, min_value: int):
        self.name = name
        self.value = value
        self.min_value = min_value

    def __str__(self):
        return f'{self.name} прямоугольника не может быть меньше {self.min_value}! Текущее значение: {self.value}.'


if __name__ == '__main__':
    rect1 = Rectangle(4, 2)
    # rect1 = Rectangle(0, 2)
    # rect2 = Rectangle(6, 2)
    rect2 = Rectangle(6, 2)
    rect3 = rect1 + rect2
    rect4 = rect1 - rect2
    print(f'rect1 = {rect1}, Периметр: {rect1.get_perimeter()}, Площадь: {rect1.get_area()}')
    print(f'rect2 = {rect2}, Периметр: {rect2.get_perimeter()}, Площадь: {rect2.get_area()}')
    print(f'rect3 = {rect3}, Периметр: {rect3.get_perimeter()}, Площадь: {rect3.get_area()}')
    print(f'rect4 = {rect4}, Периметр: {rect4.get_perimeter()}, Площадь: {rect4.get_area()}')
