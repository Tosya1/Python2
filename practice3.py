# 1. Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

import collections
import string
data_list = [1, 2, 3, 4, 3, 2, 5, 1]


def get_duplicate_list(data_list: list) -> list:
    dupl_list = []
    for i in data_list:
        if data_list.count(i) > 1 and i not in dupl_list:
            dupl_list.append(i)
    return dupl_list


print(f'Исходный список: {data_list}')
print(f'Список дублирующихся элементов: {get_duplicate_list(data_list)}')
print()

# 2. В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.


text = 'Однажды, в студеную зимнюю пору Я из лесу вышел; был сильный мороз. Гляжу, поднимается медленно в гору Лошадка, везущая хворосту воз. И шествуя важно, в спокойствии чинном, Лошадку ведет под уздцы мужичок В больших сапогах, в полушубке овчинном, В больших рукавицах… а сам с ноготок! «Здорово парнище!» - «Ступай себе мимо!» - «Уж больно ты грозен, как я погляжу! Откуда дровишки?» - «Из лесу, вестимо; Отец, слышишь, рубит, а я отвожу». (В лесу раздавался топор дровосека.) «А что, у отца-то большая семья?» - «Семья-то большая, да два человека Всего мужиков-то: отец мой да я…» - «Так вот оно что! А как звать тебя?» - «Власом». - «А кой-тебе годик?» - «Шестой миновал… Ну, мертвая!» - крикнул малюточка басом, Рванул под уздцы и быстрей зашагал.'


def get_top_frequent(text: str) -> list[str]:
    str_list = text.translate(str.maketrans(
        '', '', string.punctuation)).lower().split()
    str_dict = {}
    for i in str_list:
        str_dict.setdefault(i, str_list.count(i))
    res_list = [i[0] for i in sorted(
        str_dict.items(), key=lambda item: item[1], reverse=True)[:10]]
    return res_list


print(f'10 самых частых слов в тексте:')
[print(f'{j}) {i}') for j, i in enumerate(get_top_frequent(text), start=1)]
print()

# 3. Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# 3/1 *Верните все возможные варианты комплектации рюкзака.


max_weight = 10
things_dict = {'вещи': 2, 'еда': 3, 'вода': 2, 'оборудование': 6, 'аптечка': 1}


def get_any_set(things_dict: dict) -> list[str]:
    weight = 0
    things_list = []
    for key, value in things_dict.items():
        if value + weight <= max_weight:
            things_list.append(key)
            weight += value
    return things_list


def get_all_sets(things_dict: dict) -> list[list[str]]:
    weight = 0
    things_list = []
    i = 0
    j = 0
    sorted_dict = sorted(things_dict.items(), key=lambda x: x[1])

    while i < len(things_dict):
        things_list.append([])
        for key, value in sorted_dict:
            if value + weight <= max_weight:
                things_list[i].append(key)
                weight += value
        weight = 0
        i += 1
        sorted_dict.append(sorted_dict.pop(0))

    while j < len(things_list) - 1:
        if collections.Counter(things_list[j]) == collections.Counter(things_list[j + 1]):
            things_list.pop(j + 1)
        else:
            j += 1
    return things_list


print(f'Любой набор вещей: {", ".join(get_any_set(things_dict))} \n')
print(f'Все возможные наборы вещей:')
[print(f'{j}) {", ".join(i)}') for j, i in enumerate(get_all_sets(things_dict), start=1)]
