"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать."""

from random import randint

rand_lst = [randint(0, 100) for i in range(10)]
print(rand_lst)
max_index = rand_lst.index(max(rand_lst))
min_index = rand_lst.index(min(rand_lst))
elements_sum = 0
for i in range(max_index+1, min_index) or range(min_index+1, max_index):
    elements_sum += rand_lst[i]
print(f'сумма элементов между максимальным {rand_lst[max_index]} и минимальным {rand_lst[min_index]} = {elements_sum}')
