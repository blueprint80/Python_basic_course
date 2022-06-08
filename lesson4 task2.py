import timeit


'''В данном примере простое число проверяется перебором делителей подряд, что не очень хорошее решение.'''


def prime_number(i):
    start = timeit.default_timer()
    prime_lst = []
    num = 1
    while len(prime_lst) < i:
        flag = True
        num += 1
        for j in range(2, num):
            if num % j == 0:
                flag = False
                break
        if flag:
            prime_lst.append(num)
    return f'{i} по счету простое число - {prime_lst[-1]}\nвремя выполнения {timeit.default_timer() - start}'


'''В примере ниже делители берутся из списка простых чисел, что уменьшает количество итераций и значительно ускоряет алгоритм.'''


def prime_number_2(i):
    start = timeit.default_timer()
    prime_lst = [2]
    num = 1
    while len(prime_lst) < i:
        flag = True
        num += 1
        for j in prime_lst:
            if num % j == 0:
                flag = False
                break
        if flag:
            prime_lst.append(num)
    return f'{i} по счету простое число - {prime_lst[-1]}\nвремя выполнения {timeit.default_timer() - start}'


def eratosthene(i):
    start = timeit.default_timer()
    if i < 100:
        ind = i * 7
    elif i < 1000:
        ind = i * 10
    elif i < 10000:
        ind = i * 12
    elif i < 100000:
        ind = i * 15
    elif i < 1000000:
        ind = i * 17
    else:
        ind = i * 20

    prime_lst = []
    sieve = set(range(2, ind))
    while sieve:
        prime = min(sieve)
        sieve -= set(range(prime, ind + 1, prime))
        prime_lst.append(prime)
    if sieve == set():
        return f'{i} по счету простое число - {prime_lst[i - 1]}\nвремя выполнения {timeit.default_timer() - start}'


print(f'\nАлгоритм №1 без использованием алгоритма «Решето Эратосфена»:\n{prime_number(10000)}\n')
print(f'Алгоритм №2 без использованием алгоритма «Решето Эратосфена»:\n{prime_number_2(10000)}\n')
print(f'Алгоритм с использованием алгоритма «Решето Эратосфена»:\n{eratosthene(10000)}')
