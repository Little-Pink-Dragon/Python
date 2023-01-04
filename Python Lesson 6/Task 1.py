entered_list = input("Введите числа через пробел: ").split()
num_list = list(map(int, entered_list))
print("Список чисел, который вы ввели: ", num_list)
try:
    from math import gcd
except ImportError:
    from fractions import gcd
from functools import reduce
print(f'Наибольший общий делитель: {reduce(gcd, num_list)}')