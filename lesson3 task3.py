"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

from random import randint

rand_lst = [randint(1, 100) for i in range(10)]

max_index = rand_lst.index(max(rand_lst))
min_index = rand_lst.index(min(rand_lst))
print(f'максимальное значение(индекс) массива - {rand_lst[max_index]}({max_index})')
print(f'минимальное значение(индекс) массива - {rand_lst[min_index]}({min_index})')
print(rand_lst)
if max_index > min_index:
    rand_lst.insert(max_index, rand_lst.pop(min_index))
    rand_lst.insert(min_index, rand_lst.pop(max_index - 1))
else:
    rand_lst.insert(max_index, rand_lst.pop(min_index))
    rand_lst.insert(min_index, rand_lst.pop(max_index + 1))
print(rand_lst)
