import numpy as np
import matplotlib.pyplot as plt


def create_approximation_charts():
    numbers = np.loadtxt('numerical_data/data.txt')

    numbers_x = np.zeros(shape=21)
    numbers_f = np.zeros(shape=21)

    for i in range(21):
        numbers_x[i] = numbers[i][0]

    for i in range(21):
        numbers_f[i] = numbers[i][2]

    x = numbers_x
    y = numbers_f

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

    print(M2)
    print(W2)
    print(A2)

    # linear chart
    xN = np.linspace(0, 2, 25)
    plt.plot(xN, f(xN, A[1], A[0]), 'g-')
    plt.plot(x, y, 'ro')
    plt.xlabel('os X')
    plt.ylabel('os Y')
    plt.legend(['linear chart'])
    plt.title('approximation - linear chart')
    plt.show()

    # square chart
    xN = np.linspace(0, 2, 25)
    plt.plot(xN, f2(xN, A2[2], A2[1], A2[0]), 'r-')
    plt.plot(x, y, 'ro')
    plt.xlabel('os X')
    plt.ylabel('os Y')
    plt.legend(['square chart'])
    plt.title('approximation - square chart')
    plt.show()
