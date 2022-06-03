"""Определить, какое число в массиве встречается чаще всего."""

from random import randint

rand_lst = [randint(1, 10) for i in range(100)]
res = 0
num = 0
print(rand_lst)
for i in rand_lst:
    if res < rand_lst.count(i):
        res = rand_lst.count(i)
        num = i
print(f'число {num} встречается {res} раз(а)')
