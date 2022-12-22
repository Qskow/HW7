#4

import os

print(f'Имя операционной системы: {os.name}')
print(f'Имя Пользователя: {os.getlogin()}')
print(f'Список файлов и директорий: {os.listdir()}')

#5

import numpy as np

n = np.random.randint (0, 10, (3, 3))
print(f'Полученная матрица:{n}')

t = np.transpose(n)
print(f'транспонированная матрица:{t}')

#6

import func

a = float(input("Введите число: "))
b = float(input("Введите число: "))
print(f"{a} + {b} = {func.sum(a, b)}")
print(f"{a} - {b} = {func.diff(a, b)}")