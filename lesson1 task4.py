"""
4. Написать программу, которая генерирует в указанных пользователем границах:

    случайное целое число;
    случайное вещественное число;
    случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то
вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
from random import randint, uniform


def random_int(num1, num2):
    if (num1.isdigit() and num2.isdigit()) is False:
        raise Exception('Введено неверное число, либо введена буква!')
    elif int(num1) < int(num2):
        return randint(int(num1), int(num2))
    raise Exception('Неверный порядок ввода!')


def random_float(num1, num2):
    if (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()) is False:
        raise Exception('Введено неверное число, либо введена буква!')
    elif float(num1) < float(num2):
        return uniform(float(num1), float(num2))
    raise Exception('Неверный порядок ввода!')


def random_letter(letter1, letter2):
    if (letter1.isalpha() and letter2.isalpha()) is False:
        raise Exception('Введен неверный символ!')
    elif ord(letter1) < ord(letter2):
        return chr(randint(ord(letter1), ord(letter2)))
    raise Exception('Неверный порядок ввода или неверно выбран язык!')


if __name__ == '__main__':
    int_num1 = input('Введите два целых числа (от меньшего к большему):\nЧисло №1 - ')
    int_num2 = input('Число №2 - ')
    print(f'Случайное целое число в диапазоне {int_num1} - {int_num2}:', random_int(int_num1, int_num2), '\n')

    float_num1 = input('Введите два вещественных числа (от меньшего к большему):\nЧисло №1 - ')
    float_num2 = input('Число №2 - ')
    print(f'Случайное вещественное число в диапазоне {float_num1} - {float_num2}:', round(random_float(float_num1, float_num2), 3), '\n')

    letter_1 = input('Введите две буквы латинского алфавита (в алфавитном порядке):\nПервая буква - ')
    letter_2 = input('Вторая буква - ')
    print(f'Случайная буква в диапазоне {letter_1} - {letter_2}:', random_letter(letter_1, letter_2))
