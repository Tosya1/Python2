# 2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам
# дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random

MAX_LIMIT = 8
MIN_LIMIT = 1

# shows are the queens beaten


def is_queens_save(ls1: list[int], ls2: list[int], ls3: list[int], ls4: list[int],
                   ls5: list[int], ls6: list[int], ls7: list[int], ls8: list[int]) -> bool:
    queen_list = [ls1, ls2, ls3, ls4, ls5, ls6, ls7, ls8]
    for i in range(0, len(queen_list)):
        for j in range(i + 1, len(queen_list)):
            if queen_list[i][0] == queen_list[j][0] or queen_list[i][1] == queen_list[j][1]\
                    or abs(queen_list[i][0] - queen_list[j][0]) == abs(queen_list[i][1] - queen_list[j][1]):
                return False
    return True

# 3. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.


# сreates a random position


def create_position(min: int, max: int) -> list[int]:
    res = []
    while len(res) < max:
        pos = [random.randint(min, max), random.randint(min, max)]
        if pos not in res:
            res.append(pos)
    return res

# creates a random preprogrammed position


def create_position_programmed(min: int, max: int) -> list[int]:
    res = []
    while len(res) < max:
        pos = [random.randint(min, max), random.randint(min, max)]
        if pos not in res and pos[0] not in [i[0] for i in res] and pos[1] not in [i[1] for i in res]:
            res.append(pos)
    return res

# creates a successful sets of queens in a given amount


def get_successful_sets(count: int, min: int, max: int) -> list[list[int]]:
    res = []
    while len(res) < count:
        queen_set = create_position_programmed(min, max)
        if is_queens_save(*queen_set):
            res.append(queen_set)
    return res


if __name__ == '__main__':
    print(is_queens_save([2, 2], [3, 4], [5, 3],
          [6, 1], [1, 5], [4, 7], [7, 6], [8, 8]))
    print(is_queens_save([1, 5], [2, 2], [3, 8],
          [4, 1], [5, 4], [6, 7], [7, 3], [8, 6]))
    print(create_position(MIN_LIMIT, MAX_LIMIT))
    print(is_queens_save(*(create_position(MIN_LIMIT, MAX_LIMIT))))
    print(*(get_successful_sets(4, MIN_LIMIT, MAX_LIMIT)), sep='\n')
