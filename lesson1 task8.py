"""
8. Определить, является ли год, который ввел пользователь, високосным или невисокосным.
"""


def leap_year(year):
    if year % 4 == 0:
        return 'високосный год'
    return 'невисокосный год'


if __name__ == '__main__':
    while True:
        print(leap_year(int(input('введите год: '))))
