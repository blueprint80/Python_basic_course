"""7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число."""


def exp1(n):
    if n == 1:
        return n
    else:
        return n + exp1(n-1)


def exp2(n):
    return n * (n+1)//2


for i in range(1, 500):
    if exp1(i) == exp2(i):
        print(f'Для n={i} - True')
    else:
        print(f'Для n={i} - False')
