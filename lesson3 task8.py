"""Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой
строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу."""

matrix = []
for i in range(4):
    row = []
    matrix.append(row)
    for n in range(4):
        row.append(int(input(f'введите {n+1} число строки {i+1}: ')))
    matrix[i].append(sum(matrix[i]))
print(matrix)
for el in matrix:
    print(('{: ^4}' * 5).format(*el))
