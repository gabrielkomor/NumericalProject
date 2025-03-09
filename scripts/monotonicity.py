import numpy as np


def read_data():
    numbers = np.loadtxt('numerical_data/data.txt')
    numbers_x = np.zeros(shape=21)
    numbers_f = np.zeros(shape=21)

    for i in range(21):
        numbers_x[i] = numbers[i][0]

    for i in range(21):
        numbers_f[i] = numbers[i][2]

    return numbers_x, numbers_f


def calc_monotonicity():
    x, y = read_data()

    result = np.zeros(shape=21)
    result[0] = (y[1] - y[0]) / (x[1] - x[0])
    result[20] = (y[20] - y[19]) / (x[20] - x[19])

    for i in range(1, x.shape[0] - 1):
        result[i] = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])

    for i in range(result.shape[0]):
        if (result[i] > 0):
            print(f'The function in the vicinity of point X{i} is increasing')
        else:
            print(f'The function in the vicinity of point X{i} is decreasing')
