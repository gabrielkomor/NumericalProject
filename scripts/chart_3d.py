import numpy as np
import matplotlib.pyplot as plt


def create_3d_chart():
    numbers = np.loadtxt('numerical_data\\data.txt')

    numbers_x = np.zeros(shape=numbers.shape[0])
    numbers_y = np.zeros(shape=numbers.shape[0])
    numbers_f = np.zeros(shape=numbers.shape[0])

    for i in range(numbers.shape[0]):
        numbers_x[i] = numbers[i][0]

    for i in range(numbers.shape[0]):
        numbers_y[i] = numbers[i][1]

    for i in range(numbers.shape[0]):
        numbers_f[i] = numbers[i][2]

    x = np.ravel(numbers_x)
    y = np.ravel(numbers_y)
    z = np.ravel(numbers_f)

    plt.figure(figsize=(7, 5))
    chart = plt.axes(projection='3d')

    chart.set_box_aspect([1, 0.5, 0.5])
    chart.plot_trisurf(x, y, z, cmap='inferno')

    chart.set_xlabel('x')
    chart.set_ylabel('y')
    chart.set_zlabel('z')

    chart.view_init(40, 95)

    plt.show()
