import numpy as np
import math

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

storage = []
for i in numbers_y:
    if i not in storage:
        storage.append(i)


def sort_array(array):
    flag = True

    while flag:
        flag = False
        for item in range(array.shape[0] - 1):
            if array[item] > array[item + 1]:
                tmp = array[item]
                array[item] = array[item + 1]
                array[item + 1] = tmp
                flag = True
    return array


def calc_avg(num_y, num_f):
    res_avg = np.zeros(shape=len(storage))

    for x in range(len(storage)):
        counter = 0
        num_sum = 0
        variable = np.where(num_y == storage[x])

        for y in variable:
            for z in range(len(variable[0])):
                num_sum += num_f[y][z]
                counter += 1

        res_avg[x] = num_sum / counter
    return res_avg


def calc_median(num_y, num_f):
    res_med = np.zeros(shape=len(storage))

    for x in range(len(storage)):
        counter = 0
        variable = np.where(num_y == storage[x])

        for y in variable:
            tmp = np.zeros(shape=len(variable[0]))
            for z in range(len(variable[0])):
                tmp[z] = num_f[y][z]
                counter += 1

            tmp = sort_array(tmp)

        res_med[x] = tmp[round(counter / 2)]
    return res_med


def calc_deviation(num_y, num_f, res_avg):
    res_dev = np.zeros(shape=len(storage))

    for x in range(len(storage)):
        value = 0
        variable = np.where(num_y == storage[x])

        for y in variable:
            tmp = np.zeros(shape=len(variable[0]))
            for z in range(len(variable[0])):
                tmp[z] = num_f[y][z]

            for c in range(tmp.shape[0]):
                value += (tmp[c] - res_avg[x]) ** 2
            value /= tmp.shape[0]

        res_dev[x] = math.sqrt(value)
    return res_dev


def calc_med_mea_dev():
    avg_result = calc_avg(numbers_y, numbers_f)
    median_result = calc_median(numbers_y, numbers_f)
    dev_result = calc_deviation(numbers_y, numbers_f, avg_result)

    print('avg values: ', '\t\t\t\t\t\tmedian: ', '\t\t\t\tstandard deviation: ')
    for index in range(avg_result.shape[0]):
        print(f'For Y {storage[index]}: {avg_result[index]} \t\t', end='')
        print(f'For Y {storage[index]}: {median_result[index]} \t\t', end='')
        print(f'For Y {storage[index]}: {dev_result[index]}')
