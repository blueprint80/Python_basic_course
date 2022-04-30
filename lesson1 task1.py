"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


def num_sum_multy(num):
    if 99 < num < 1000:
        a = num // 100
        b = num // 10 % 10
        c = num % 10
        return f'сумма: {a + b + c}\nпроизведение: {a * b * c}'
    raise Exception('введено неверное число')


if __name__ == '__main__':
    print(num_sum_multy(int(input())))
