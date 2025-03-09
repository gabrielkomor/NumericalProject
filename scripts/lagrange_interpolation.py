import numpy as np
import matplotlib.pyplot as plt


def read_data():
    numbers = np.loadtxt('numerical_data\\data.txt')
    numbers_x = np.zeros(shape=21)
    numbers_f = np.zeros(shape=21)

    for i in range(21):
        numbers_x[i] = numbers[i][0]

    for i in range(21):
        numbers_f[i] = numbers[i][2]

    return numbers_x, numbers_f


def denominator(i, y):
    m = 1
    for j in range(y.shape[0]):
        if i != j:
            m *= y[i] - y[j]
    return m


def interpolation(x, y):
    n = x.shape[0]
    a = np.zeros(n)
    for i in range(n):
        a[i] = y[i] / denominator(i, x)
    return a


def function(a, x, xi):
    w = 0
    for i in range(x.shape[0]):
        m = 1
        for j in range(x.shape[0]):
            if i != j:
                m *= (xi - x[j])
        w += a[i] * m
    return w


def draw_lag(xp, xk, x, y):
    A = interpolation(x, y)
    lP = 100
    xt = np.linspace(xp, xk, lP)
    yt = np.zeros(xt.shape[0])

    for i in range(xt.shape[0]):
        yt[i] = function(A, x, xt[i])

    plt.plot(x, y, 'bo', label='[x, y]')
    plt.plot(xt, yt, 'r-', linewidth=0.2, label='[function 2]')
    plt.plot(xt, yt, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Lagrange's interpolation")


def lagrange_interpolation():
    x, y = read_data()

    x1 = np.array([x[0], x[1], x[2], x[3], x[4], x[5]])
    y1 = np.array([y[0], y[1], y[2], y[3], y[4], y[5]])

    x2 = np.array([x[5], x[6], x[7], x[8], x[9], x[10]])
    y2 = np.array([y[5], y[6], y[7], y[8], x[9], y[10]])

    x3 = np.array([x[10], x[11], x[12], x[13], x[14], x[15]])
    y3 = np.array([y[10], y[11], y[12], y[13], y[14], y[15]])

    x4 = np.array([x[15], x[16], x[17], x[18], x[19], x[20]])
    y4 = np.array([y[15], y[16], y[17], y[18], y[19], y[20]])

    draw_lag(0, 0.5, x1, y1)
    draw_lag(0.5, 1, x2, y2)
    draw_lag(1, 1.5, x3, y3)
    draw_lag(1.5, 2, x4, y4)

    plt.show()
