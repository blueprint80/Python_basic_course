"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве."""

from random import randint

rand_lst = [randint(-100, 100) for i in range(10)]

print(rand_lst)
ind = -1
negative_num_lst = []
for i in rand_lst:
    ind += 1
    if i < 0:
        negative_num_lst.append(i)

print(f'максимальный отрицательный элемент: {max(negative_num_lst)}, индекс {rand_lst.index(max(negative_num_lst))}')
