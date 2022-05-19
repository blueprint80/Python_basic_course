"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр."""


def sum_n(n):
    total = 0
    for i in n:
        total += int(i)
    return total


sum2 = ''
res_num = ''
while True:
    num = input('введите число, для окончания ввода нажмите Enter: ')
    sum1 = sum_n(num)
    if num == '':
        break
    elif sum2 == '':
        sum2 = sum1
        res_num = num
    elif int(sum1) > int(sum2):
        sum2 = sum1
        res_num = num
    else:
        continue
print(f'наибольшее по сумме цифр число - {res_num}\nсумма цифр - {sum2}')
