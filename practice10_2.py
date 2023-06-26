# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from pathlib import Path


class GroupRename:
    def __init__(self, new_name: str, digits_count: int, ext: str, new_ext: str, name_range: list[int]):
        self.new_name = new_name
        self.digits_count = digits_count
        self.ext = ext
        self.new_ext = new_ext
        self.name_range = name_range

    def _create_number(self, n: int) -> str:
        if len(str(n)) < self.digits_count:
            return (self.digits_count - len(str(n)))*'0' + str(n)
        else:
            return str(n)

    def _check_name_range(self, name: str) -> list[int]:
        if len(name) >= self.name_range[1]:
            return [self.name_range[0]-1, self.name_range[1]]
        elif len(name) < self.name_range[0]:
            return [0, 0]
        elif len(name) >= self.name_range[0] and len(name) - 1 < self.name_range[1]:
            return [self.name_range[0] - 1, len(name)]

    def rename_files(self) -> None:
        p = Path(Path().cwd())
        i = 1
        for file in p.iterdir():
            if file.name.endswith('.' + self.ext):
                name = file.name.partition('.')[0]
                name_rng = self._check_name_range(name)
                name = name[name_rng[0]: name_rng[1]] + self.new_name + \
                    self._create_number(i) + '.' + self.new_ext
                Path(file.name).rename(name)
                i += 1


if __name__ == '__main__':
    renamer = GroupRename('file', 3, 'rtf', 'txt',  [1, 3])
    renamer.rename_files()
