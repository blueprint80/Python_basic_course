"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите
на экран исходный и отсортированный массивы."""

from random import uniform


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] <= lst[1]:
            return lst
        else:
            return lst[::-1]
    else:
        return merge(merge_sort(lst[:len(lst)//2]), merge_sort(lst[len(lst)//2:]))


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        res.extend(left[i:])
    else:
        res.extend(right[j:])
    return res


if __name__ == '__main__':
    random_lst = [uniform(0, 50) for i in range(10)]
    print(f'массив до сортировки:\n{random_lst}')
    print(f'массив после сортировки:\n{merge_sort(random_lst)}')
