"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""


def middle_num(a, b, c):
    if b < a < c or c < a < b:
        return f'среднее: {a}'
    elif a < b < c or c < b < a:
        return f'среднее: {b}'
    return f'среднее: {c}'


if __name__ == '__main__':
    print(middle_num(int(input('первое число: ')),
                     int(input('второе число: ')),
                     int(input('третье число: '))))
