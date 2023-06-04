# 1. Напишите функцию для транспонирования матрицы


matrix = [[2, 8, 16], [3, 9, 21]]


def transpose_matrix(matrix: list[list]) -> list[list]:
    return [list(i) for i in zip(*matrix)]


print(f'Исходная матрица: {matrix}')
print(f'Транспонированная матрица: {transpose_matrix(matrix)}')

# 2. Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def get_param_dict(**kwargs):
    params_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set,bytearray)):
            params_dict.setdefault(str(value), key)
        else:
            params_dict.setdefault(value, key)
    return params_dict


print(get_param_dict(param1='value1', param2=2,
      param3=[1, 3, 4, 5], param4=True))

# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
import decimal

LIMIT = 50
WEALTH_LIMIT = 5000
WEALTH_PERS = decimal.Decimal(0.1)
SUB_PERS = decimal.Decimal(0.015)
SUB_PERS_MAX = 600
SUB_PERS_MIN = 30
OPER_LIMIT = 3
OPER_PERS = decimal.Decimal(0.03)
deposit = decimal.Decimal(0).quantize(decimal.Decimal("1.00"))
trans_count = 0
trans_list = []


def check_limit(sum: int | decimal.Decimal) -> int:
    return sum % LIMIT


def get_tax(sum: int | decimal.Decimal) -> decimal.Decimal:
    wealth_tax = decimal.Decimal(
        sum * WEALTH_PERS).quantize(decimal.Decimal("1.00"))
    return (wealth_tax)


def get_charge_pers(sum: int | decimal.Decimal) -> decimal.Decimal:
    charge_pers = decimal.Decimal(
        sum * SUB_PERS).quantize(decimal.Decimal("1.00"))
    if charge_pers < SUB_PERS_MIN:
        charge_pers = SUB_PERS_MIN
    elif charge_pers > SUB_PERS_MAX:
        charge_pers = SUB_PERS_MAX
    return charge_pers


def top_up():
    global deposit, trans_count
    add_sum = int(input('Введите сумму пополнения: '))
    if check_limit(add_sum):
        print(f'Сумма пополнения должна быть кратна {LIMIT}!')
    elif deposit + add_sum > WEALTH_LIMIT:
        wealth_tax = get_tax(add_sum)
        deposit += add_sum - wealth_tax
        trans_count += 1
        print(f'Удержаны налоги на богатство {wealth_tax}')
        trans_list.append(add_sum)
        trans_list.append(- wealth_tax)
    else:
        deposit += add_sum
        trans_count += 1
        trans_list.append(add_sum)


def charge():
    global deposit, trans_count
    sub_sum = int(input('Введите сумму снятия: '))
    sub_pers_sum = get_charge_pers(sub_sum)

    if sub_sum + sub_pers_sum > deposit:
        print(
            f'Сумма снятия {sub_sum + sub_pers_sum } превышает доступрую сумму {deposit} !')
    elif check_limit(sub_sum):
        print(f'Сумма снятия должна быть кратна {LIMIT}!')
    elif deposit > WEALTH_LIMIT:
        wealth_tax = get_tax(sub_sum)
        deposit -= sub_sum - wealth_tax
        trans_count += 1
        trans_list.append(-sub_sum)
        trans_list.append(-sub_pers_sum)
        trans_list.append(- wealth_tax)
        print(f'Удержан % за снятие {sub_pers_sum}')
        print(f'Удержаны налоги на богатство {wealth_tax}')
    else:
        deposit = deposit - sub_sum - sub_pers_sum
        trans_count += 1
        trans_list.append(-sub_sum)
        trans_list.append(-sub_pers_sum)
        print(f'Удержан % за снятие {sub_pers_sum}')


def add_oper_bonus():
    global deposit
    if trans_count != 0 and not trans_count % OPER_LIMIT:
        oper_pers_sum = decimal.Decimal(
            deposit * OPER_PERS).quantize(decimal.Decimal("1.00"))
        deposit = decimal.Decimal(deposit) + oper_pers_sum
        trans_list.append(oper_pers_sum)
        print(f'Начислен операционный %: {oper_pers_sum}')


def run():
    while True:
        action = input(
            'Выберите действие:\n1 - пополнить\n2 - снять\n3 - выйти \n')
        if action == '1':
            top_up()
        elif action == '2':
            charge()
        elif action == '3':
            quit()
        add_oper_bonus()
        print(f'Остаток на счете: {deposit}')



run()
