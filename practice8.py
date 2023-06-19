# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import csv
import json
import os
from pathlib import Path
import pickle


def get_dir_size(dir: str, data: list[dict]) -> int:
    size = 0
    for i in data:
        if i['parent'] == dir:
            size += i['size']
    return size


def get_data(path: str | Path) -> list[dict]:
    files_list = []
    data = []
    for dir_path, dir_name, file_name in os.walk(path):
        files_list.append([dir_path, dir_name, file_name])

    for i in files_list:
        for j in i[2]:
            data.append({'name': j, 'type': 'file', 'parent': i[0].split(
                '\\')[-1], 'size': os.path.getsize(f'{i[0]}\\{j}')})
    for i in files_list:
        for j in i[1]:
            data.append({'name': j, 'type': 'dir', 'parent': i[0].split(
                '\\')[-1], 'size': get_dir_size(j, data)})
    return data


def write_json(file: str | Path, data: list[dict]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def write_csv(file: str | Path, data: list[dict]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=['name', 'type', 'parent', 'size'])
        writer.writeheader()
        writer.writerows(data)


def write_pickle(file: str | Path, data: list[dict]) -> None:
    with open(file, 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    write_json('data.json', get_data(Path.cwd()))
    write_csv('data.csv', get_data(Path.cwd()))
    write_pickle('data.pickle', get_data(Path.cwd()))
