import timeit

'''В примере ниже в процессе выполнения цикла, за одну итерацию, в строку "rev_num" добавляется по одному символу из "перевернутой" строки
"num", т.е. производится проход по n элементам строки. Сложность данного алгоритма - О(n)'''


def rev(num):
    start = timeit.default_timer()
    rev_num = ''
    for i in reversed(str(num)):
        rev_num += i
    return f'время выполнения {timeit.default_timer() - start}'


test = 123456789 ** 50000
print(rev(str(test)))
