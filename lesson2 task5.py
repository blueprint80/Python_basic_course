"""5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в
табличной форме: по десять пар "код-символ" в каждой строке."""

string_length = 1
for char in range(32, 128):
    if string_length // 10 == 1:
        print(f'{char:5}: {chr(char)}  \033[36m|\033[0m')
        string_length = 0
    else:
        print(f'{char:5}: {chr(char)}  \033[36m|\033[0m', end=" ")
    string_length += 1
