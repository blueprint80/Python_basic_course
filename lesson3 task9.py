"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

from random import randint

string_length = int(input('длина строки: '))
row_number = int(input("столбцы: "))

rand_matrix = [[randint(1, 100) for i in range(string_length)] for n in range(row_number)]
min_list = []
column_list = []

for element in range(string_length):
    row_temp = []
    for row in range(row_number):
        row_temp.append(rand_matrix[row][element])
    column_list.append(row_temp)

for i in column_list:
    min_list.append(min(i))

for n in rand_matrix:
    print(('{: ^4}' * string_length).format(*n))

print('\nминимальные элементы столбцов матрицы:', *min_list)
print(f'максимальный элемент среди минимальных элементов столбцов матрицы: {max(min_list)}')
