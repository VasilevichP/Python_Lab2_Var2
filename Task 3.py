import random

import numpy as np


def find_max_index(arr):
    max_row=max(arr,key=max)
    return arr.index(max_row),max_row.index(max(max_row))


rows = random.randint(1, 6)
print("Количество строк:", rows)
cols = random.randint(1, 6)
print("Количество столбцов:", cols)
matrix=[]
for i in range(rows):
    matrix.append([random.randint(1,99) for i in range(cols)])
print(matrix)
print(find_max_index(matrix))
