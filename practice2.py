#1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX: int = 16
num: int = int(input('Введите целое число: '))

def rev (num: int) -> str:
    rev_num = ''
    while num  >= 1:
        char = num % HEX
        if char < 10 or char == 16:
            rev_num += str(num % HEX)  
        elif char == 10:
            rev_num += 'a'  
        elif char == 11:
            rev_num += 'b' 
        elif char == 12:
            rev_num += 'c'
        elif char == 13:
            rev_num += 'd' 
        elif char == 14:
            rev_num += 'e'
        elif char == 15:
            rev_num += 'f'           
        num = num // HEX  
    return rev_num[::-1]

print(f'Число {num} в шестнадцатеричной системе - {rev(num)}')
print(f'Проверка: {hex(num)}')

#2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа
# должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

fraction1: list[str, str] = input('Введите дробь вида “a/b”: ').split('/')
fraction2: list[str, str] = input('Введите дробь вида “a/b”: ').split('/')
numerator1: int = int(fraction1[0])
numerator2: int = int(fraction2[0])
denominator1: int = int(fraction1[1])
denominator2: int = int(fraction2[1])

def sum (numerator1: int, denominator1: int, numerator2: int, denominator2: int) -> str:
    denominator = int(denominator1 * denominator2) // get_gcd(denominator1, denominator2)
    numerator = int(numerator1 * (denominator / denominator1) + numerator2 * (denominator / denominator2))
    if get_gcd(numerator, denominator) !=1:
        gcd = get_gcd(numerator, denominator)
        numerator /= gcd
        denominator /= gcd   
    if not numerator % denominator:
        return str(int(numerator / denominator))
    else:
        return str(f'{int(numerator)}/{int(denominator)}')
    
def mult(numerator1: int, denominator1: int, numerator2: int, denominator2: int) -> str:
    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    if get_gcd(numerator, denominator) !=1:
        gcd = get_gcd(numerator, denominator)
        numerator /= gcd
        denominator /= gcd
    if not numerator % denominator:
        return str(int(numerator / denominator))
    else:
        return str(f'{int(numerator)}/{int(denominator)}')
    
def get_gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
          
print(f'Сумма дробей: {sum(numerator1, denominator1,numerator2, denominator2)}')
print(f'Проверка суммы: {fractions.Fraction(numerator1, denominator1) + fractions.Fraction(numerator2, denominator2)}')
print(f'Произведение дробей: {mult(numerator1, denominator1,numerator2, denominator2)}')
print(f'Проверка произведения: {fractions.Fraction(numerator1, denominator1) * fractions.Fraction(numerator2, denominator2)}')
