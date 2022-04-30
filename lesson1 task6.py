"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


def letter(num):
    if num in range(1, 27):
        return f'буква под номером {num} - {chr(num + ord("a") - 1)}'
    raise Exception('out of range')


if __name__ == '__main__':
    while True:
        print(letter(int(input('введите номер буквы в алфавите: '))))
