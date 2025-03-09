import numpy as np
import math


def read_data():
    numbers = np.loadtxt('numerical_data/data.txt')

    numbers_x = np.zeros(shape=numbers.shape[0])
    numbers_y = np.zeros(shape=numbers.shape[0])
    numbers_f = np.zeros(shape=numbers.shape[0])

    for i in range(numbers.shape[0]):
        numbers_x[i] = numbers[i][0]

    for i in range(numbers.shape[0]):
        numbers_y[i] = numbers[i][1]

    for i in range(numbers.shape[0]):
        numbers_f[i] = numbers[i][2]

    return numbers_x, numbers_y, numbers_f


def calc_area(x1, x2, x3, y1, y2, y3, z1, z2, z3):
    numbers_x, numbers_y, numbers_f = read_data()
    a = np.array([numbers_x[x1], numbers_y[y1], numbers_f[z1]])
    b = np.array([numbers_x[x2], numbers_y[y2], numbers_f[z2]])
    c = np.array([numbers_x[x3], numbers_y[y3], numbers_f[z3]])

    ab = np.array([b[0] - a[0], b[1] - a[1], b[2] - a[2]])
    ac = np.array([c[0] - a[0], c[1] - a[1], c[2] - a[2]])

    wyz1 = ab[1] * ac[2] - ab[2] * ac[1]
    wyz2 = -(ab[0] * ac[2] - ab[2] * ac[0])
    wyz3 = ab[0] * ac[1] - ab[1] * ac[0]

    area = 0.5 * math.sqrt(pow(wyz1, 2) + pow(wyz2, 2) + pow(wyz3, 2))
    return area


def calculate_figure_area():
    suma = 0
    for z in range(0, 20):
        for i in range(z, 210, 21):
            suma += calc_area(i, i + 1, i + 21, i, i + 1, i + 21, i, i + 1, i + 21)
            suma += calc_area(i + 1, i + 1, i + 21, i + 21, i + 1, i + 21, i + 22, i + 1, i + 21)

    print(f'Area of the figure: {suma}')
