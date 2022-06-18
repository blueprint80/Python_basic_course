"""Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент
ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно
решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках"""

from random import randint


def median(lst):
    lst = lst.copy()
    i = 0
    while i < len(lst) - 1:
        lst.remove(min(lst))
        lst.remove(max(lst))
    return f'медиана массива: {lst[0]}'
# не очень удачный вариант кода, особенно для больших массивов.


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
    random_lst = [randint(0, 100) for i in range(2 * randint(2, 10) - 1)]
    print(f'массив до сортировки:\n{random_lst}')
    print(median(random_lst))
    print(f'\nмассив после сортировки:\n{merge_sort(random_lst)}')
    print(f'медиана массива: {merge_sort(random_lst)[len(merge_sort(random_lst))//2]}')
