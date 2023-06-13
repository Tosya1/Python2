
**1.1** Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

**1.2** Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

**1.3** Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

**2.1** Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

**2.2** Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

**3.1** Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

**3.2** В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

**3.3** Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.  
*Верните все возможные варианты комплектации рюкзака.

**4.1** Напишите функцию для транспонирования матрицы

**4.2** Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.

**4.3** Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.  
Напишите программу банкомат.  
✔ Начальная сумма равна нулю  
✔ Допустимые действия: пополнить, снять, выйти  
✔ Сумма пополнения и снятия кратны 50 у.е.  
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.  
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%  
✔ Нельзя снять больше, чем на счёте  
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной  
✔ Любое действие выводит сумму денег

**5.1** Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

**5.2** Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

**5.3** Создайте функцию генератор чисел Фибоначчи (см. Википедию)

**6.1** Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY  
Функция возвращает истину, если дата может существоватьили ложь, если такая дата невозможна.  
Для простоты договоримся, что год может быть в диапазоне [1, 9999].  
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.  
Проверку года на високосность вынести в отдельную защищённую функцию.  
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

**6.2** Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.  
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.   
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.   
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.  
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

**6.3** Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.

**7.1** Напишите функцию группового переименования файлов. Она должна:  
✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.  
✔ принимать параметр количество цифр в порядковом номере.  
✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.  
✔ принимать параметр расширение конечного файла.  
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.  

Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


