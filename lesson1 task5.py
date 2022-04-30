"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""


def letters_num(letter):
    a = ord('a')
    return ord(letter) - a + 1


def letters_gap(letter1, letter2):
    if letter1 in 'abcdefghijklmnopqrstuvwxyz' and letter2 in 'abcdefghijklmnopqrstuvwxyz':
        if letter1 < letter2:
            return f'номер буквы: {letter1} - {letters_num(letter1)}\n'\
                   f'номер буквы: {letter2} - {letters_num(letter2)}\n'\
                   f'количество букв между: {letter1} и {letter2} - {letters_num(letter2) - letters_num(letter1) - 1}'
        elif letter1 > letter2:
            return f'номер буквы: {letter1} - {letters_num(letter1)}\n'\
                   f'номер буквы: {letter2} - {letters_num(letter2)}\n'\
                   f'количество букв между: {letter1} и {letter2} - {letters_num(letter1) - letters_num(letter2) - 1}'
        raise Exception('введены одинаковые буквы')
    raise Exception('введен неверный символ')


print(letters_gap(input('введите первую букву английского алфавита: '),
                  input('введите вторую букву английского алфавита: ')))
