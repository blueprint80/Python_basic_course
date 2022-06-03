"""В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными),
так и различаться."""

from random import randint


def min_num(lst):
    return lst.pop(lst.index(min(lst)))


rand_lst = [randint(0, 100) for i in range(10)]
print(rand_lst)
min_1 = min_num(rand_lst)
min_2 = min_num(rand_lst)
print(f'первый наименьший элемент {min_1}\nвторой наименьший элемент {min_2}')
