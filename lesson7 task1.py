"""Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм
(сделайте его умнее)."""

from random import randint

# временная сложность O(n^2)
# пространственная сложность O(1)


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        count = 0  # уменьшает кол-во итераций
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                count += 1
        if count == 0:
            break
    return lst


if __name__ == '__main__':
    random_lst = [randint(-100, 100) for i in range(10)]
    print(f'массив до сортировки:\n{random_lst}')
    print(f'массив после сортировки:\n{bubble_sort(random_lst)}')
