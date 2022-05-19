"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5)."""


def numbers_counter(num):
    even_counter = 0
    odd_counter = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    return f'количество четных цифр в числе {num}: {even_counter}\nколичество нечетных цифр в числе {num}: {odd_counter}'


if __name__ == '__main__':
    print(numbers_counter(34560))
