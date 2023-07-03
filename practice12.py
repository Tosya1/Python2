# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv
from pathlib import Path


class Validation:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.isalpha():
            raise ValueError(
                f'Значение {value}  должно содержать только буквы')
        if not value.istitle():
            raise ValueError(
                f'Значение {value}  должно начинаться с заглавной буквы')


class Range:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if isinstance(value, list):
            for i in value:
                self.validate(i)
        else:
            self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if value not in range(self.min_value, self.max_value + 1):
            raise ValueError(
                f'Значение {value} должно быть в диапазоне от {self.min_value} до {self.max_value}')


class Course:
    MIN_SCORE = 2
    MAX_SCORE = 5
    MIN_TEST_RES = 0
    MAX_TEST_RES = 100
    _scores = Range(MIN_SCORE, MAX_SCORE)
    _tests_res = Range(MIN_TEST_RES, MAX_TEST_RES)

    def __init__(self, name: str, scores: list[int] = [], tests_res: list[int] = []):
        self.name = name
        self._scores = scores
        self._tests_res = tests_res

    @property
    def scores(self):
        return self._scores

    @property
    def tests_res(self):
        return self._tests_res

    def add_score(self, score: int) -> None:
        Range(self.MIN_SCORE, self.MAX_SCORE).validate(score)
        self._scores.append(score)

    def add_test_res(self, test_res: int) -> None:
        Range(self.MIN_TEST_RES, self.MAX_TEST_RES).validate(test_res)
        self._tests_res.append(test_res)


class Student:
    name = Validation()
    middle_name = Validation()
    last_name = Validation()

    def __init__(self, name: str, middle_name: str, last_name: str, courses_file: str | Path):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self._courses_file = courses_file
        self._courses_name = self._get_courses()
        self.scores_dict = {}
        self.tests_res_dict = {}

    def _get_courses(self) -> list[str]:
        with open(self._courses_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            return [i[0] for i in [*reader]]

    def add_to_courses_dicts(self, course: Course) -> None:
        if course.name in self._courses_name:
            self.scores_dict.setdefault(course.name, course.scores)
            self.tests_res_dict.setdefault(course.name, course.tests_res)
        else:
            raise ValueError(
                f'Предмета {course.name} нет в списке учебных предметов')

    def get_avr_tests_res(self) -> dict[str, float]:
        tests_avr_dict = {}
        for key, value in self.tests_res_dict.items():
            if value != []:
                tests_avr_dict.setdefault(
                    key, round(sum(value) / len(value), 1))
            else:
                tests_avr_dict.setdefault(key, 0)
        return tests_avr_dict

    def get_avr_score(self) -> float:
        all_scores = [j for i in [*self.scores_dict.values()] for j in i]
        return round((sum(all_scores) / len(all_scores)), 1)

    def __str__(self) -> str:
        return f'{self.last_name} {self.name} {self.middle_name}, \
            \nОценки:\n{self.param_dict_to_str(self.scores_dict)} \
            \n________________________________________________\
            \nРезультаты тестов:\n{self.param_dict_to_str(self.tests_res_dict)} \
            \n________________________________________________'

    def param_dict_to_str(self, dict: dict[str, list[int]]) -> str:
        return "\n".join([f'{k}: {", ".join([str(i) for i in v])}' for k, v in dict.items()])

    def avr_dict_to_str(self, dict: dict[str, float]) -> str:
        return "\n".join([f'{k}: {v}' for k, v in dict.items()])


if __name__ == '__main__':
    s1 = Student('Иван', 'Иванович', 'Иванов', 'courses.csv')
    c1 = Course('Математика', [3, 5, 4], [100, 75, 65, 80])
    c2 = Course('Физика', [3, 5, 4], [100, 75, 65, 80])
    c3 = Course('Химия')
    s1.add_to_courses_dicts(c1)
    s1.add_to_courses_dicts(c2)
    s1.add_to_courses_dicts(c3)
    # c2.add_score(6)
    c2.add_score(5)
    c3.add_score(4)
    # c1.add_test_res(-100)
    c1.add_test_res(100)
    c3.add_test_res(75)
    print(s1)
    print(
        f'Средние результаты тестов по предметам:\n{s1.avr_dict_to_str(s1.get_avr_tests_res())}')
    print(f'Средняя оценка по всем предметам: {s1.get_avr_score()}')
