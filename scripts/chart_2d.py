import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


def create_2d_chart():
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

    xi = np.linspace(numbers_x.min(), numbers_x.max(), 1000)
    yi = np.linspace(numbers_y.min(), numbers_y.max(), 1000)

    zi = griddata((numbers_x, numbers_y), numbers_f, (xi[None, :], yi[:, None]), method='cubic')

    z_min = numbers_f.min()
    z_max = numbers_f.max()

    plt.contourf(xi, yi, zi, 15, cmap=plt.cm.rainbow, vmax=z_max, vmin=z_min)

    plt.axis('equal')
    plt.title('2D chart')

    plt.colorbar()
    plt.show()
