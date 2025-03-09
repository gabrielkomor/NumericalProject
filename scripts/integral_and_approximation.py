import numpy as np


def lagrange_area(x, y):
    suma = 0

    for i in range(x.shape[0] - 1):
        height = abs(x[i] - x[i + 1])
        base_a = (y[i])
        base_b = (y[i + 1])
        area = 0.5 * (base_a + base_b) * height
        suma += area

    return suma


def read_data():
    numbers = np.loadtxt('numerical_data/data.txt')
    numbers_x = np.zeros(shape=21)
    numbers_f = np.zeros(shape=21)

    for i in range(21):
        numbers_x[i] = numbers[i][0]

    for i in range(21):
        numbers_f[i] = numbers[i][2]

    return numbers_x, numbers_f


def denominator(i, x):
    m = 1
    for j in range(x.shape[0]):
        if i != j:
            m *= x[i] - x[j]
    return m


def interp_lagA(x, y):
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
    A = interp_lagA(x, y)
    lP = 100
    xt = np.linspace(xp, xk, lP)
    yt = np.zeros(xt.shape[0])

    for i in range(xt.shape[0]):
        yt[i] = function(A, x, xt[i])

    return xt, yt


def calc_integral_and_approx():
    x, y = read_data()

    x1 = np.array([x[0], x[1], x[2], x[3], x[4], x[5]])
    y1 = np.array([y[0], y[1], y[2], y[3], y[4], y[5]])

    x2 = np.array([x[5], x[6], x[7], x[8], x[9], x[10]])
    y2 = np.array([y[5], y[6], y[7], y[8], x[9], y[10]])

    x3 = np.array([x[10], x[11], x[12], x[13], x[14], x[15]])
    y3 = np.array([y[10], y[11], y[12], y[13], y[14], y[15]])

    x4 = np.array([x[15], x[16], x[17], x[18], x[19], x[20]])
    y4 = np.array([y[15], y[16], y[17], y[18], y[19], y[20]])

    xt1, yt1 = draw_lag(0, 0.5, x1, y1)
    xt2, yt2 = draw_lag(0.5, 1, x2, y2)
    xt3, yt3 = draw_lag(1, 1.5, x3, y3)
    xt4, yt4 = draw_lag(1.5, 2, x4, y4)

    area1 = lagrange_area(xt1, yt1)
    area2 = lagrange_area(xt2, yt2)
    area3 = lagrange_area(xt3, yt3)
    area4 = lagrange_area(xt4, yt4)

    area = area1 + area2 + area3 + area4

    print(f'interpolation result (split into 4 intervals): {area}')

    M = np.zeros(shape=(2, 2))
    W = np.zeros(shape=2)

    M2 = np.zeros(shape=(3, 3))
    W2 = np.zeros(shape=3)

    for i in range(x.size):
        M2[0][0] = x.size
        M2[0][1] += x[i]
        M2[0][2] += x[i] * x[i]
        M2[1][0] += x[i]
        M2[1][1] += x[i] * x[i]
        M2[1][2] += x[i] * x[i] * x[i]
        M2[2][0] += x[i] * x[i]
        M2[2][1] += x[i] * x[i] * x[i]
        M2[2][2] += x[i] * x[i] * x[i] * x[i]

    for i in range(y.size):
        W2[0] += y[i]
        W2[1] += x[i] * y[i]
        W2[2] += x[i] * x[i] * y[i]

    A2 = np.linalg.solve(M2, W2)

    for i in range(x.size):
        M[0][0] = x.size
        M[0][1] += x[i]
        M[1][0] += x[i]
        M[1][1] += x[i] * x[i]

    for i in range(y.size):
        W[0] += y[i]
        W[1] += x[i] * y[i]

    A = np.linalg.solve(M, W)

    def f(x, a1, a0):
        return a1 * x + a0

    def f2(x, a2, a1, a0):
        return a2 * x * x + a1 * x + a0

    xN = np.linspace(0, 2, 25)
    linear_area = lagrange_area(xN, f(xN, A[1], A[0]))
    quadric_square = lagrange_area(xN, f2(xN, A2[2], A2[1], A2[0]))

    print(f'approximation result (linear function): {linear_area}')
    print(f'result approximation (quadratic function): {quadric_square}')
