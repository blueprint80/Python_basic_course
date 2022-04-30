"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
"""


def line(x1, y1, x2, y2):
    k = (y2 - y1)/(x2 - x1)
    b = y1 - k * x1
    return f'y = {k}x + {b}'


if __name__ == '__main__':
    print(line(int(input('x1 = ')),
               int(input('y1 = ')),
               int(input('x2 = ')),
               int(input('y2 = '))))
