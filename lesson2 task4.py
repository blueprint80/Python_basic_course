"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры."""


def range_sum(num):
    total = 0
    num_range = 1
    counter = 0
    while counter < num:
        total += num_range
        counter += 1
        num_range /= -2
    return total


if __name__ == '__main__':
    print(range_sum(int(input('введите количество элементов: '))))
