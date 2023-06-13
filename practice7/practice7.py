#✔ Напишите функцию группового переименования файлов. Она должна:
#✔ принимать параметр желаемое конечное имя файлов.
#При переименовании в конце имени добавляется порядковый номер.
#✔ принимать параметр количество цифр в порядковом номере.
#✔ принимать параметр расширение исходного файла.
#Переименование должно работать только для этих файлов внутри каталога.
#✔ принимать параметр расширение конечного файла.
#✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
#[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
#желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from pathlib import Path

def create_number(n: int, digits_count: int) -> str:
    if len(str(n)) < digits_count:
        return (digits_count - len(str(n)))*'0' + str(n)
    else:
        return str(n)

def check_name_range(string: str, range: list[int]) -> list[int]:
    if len(string) >= range[1]:
        return [range[0]-1, range[1]]
    elif len(string) < range[0]:
        return [0, 0]
    elif len(string) >= range[0] and len(string) - 1 < range[1]:
        return [range[0] - 1, len(string)]

def rename_files(new_name: str, digits_count: int, ext: str, new_ext: str, name_range: list[int]) -> None:
    p = Path(Path().cwd())
    i = 1
    for file in p.iterdir():
        if file.name.endswith('.' + ext):
            name = file.name.partition('.')[0]
            name_rng = check_name_range(name, name_range)
            name = name[name_rng[0]: name_rng[1]] + new_name +  create_number(i, digits_count) + '.' + new_ext
            Path(file.name).rename(name)
            i += 1

if __name__ == '__main__':
    rename_files('file', 3, 'txt', 'rtf',  [2, 3])

