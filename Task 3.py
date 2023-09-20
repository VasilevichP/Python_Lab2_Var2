import random

import numpy as np


def find_max_index(arr):
    max_value = arr[0][0]
    max_row = 0
    max_col = 0

    for row in range(len(arr)):
         k=max(arr[row])
         if k>max_value:
            max_value=k
            max_row=row
            max_col=arr[row].index(k)

    print("Индексы первого вхождения максимального элемента: [", max_row,"][", max_col,"]")


rows = random.randint(1, 6)
print("Количество строк:", rows)
cols = random.randint(1, 6)
print("Количество столбцов:", cols)
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        a = random.randint(10, 99)
        row.append(a)
    matrix.append(row)
    print(row)
find_max_index(matrix)
