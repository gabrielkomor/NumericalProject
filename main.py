from scripts.chart_2d import create_2d_chart
from scripts.chart_3d import create_3d_chart
from scripts.med_mea_dev import calc_med_mea_dev
from scripts.lagrange_interpolation import lagrange_interpolation
from scripts.approximation_functions import create_approximation_charts
from scripts.area_function import calculate_figure_area
from scripts.integral_and_approximation import calc_integral_and_approx
from scripts.partial_derivatives import calc_partial_derivatives
from scripts.monotonicity import calc_monotonicity

print()
print('Enter the task number you want to display <1 - 9>')
print('1 - 2D plot')
print('2 - 3D plot')
print('3 - median, mean, standard deviation')
print('4 - Lagrange interpolation')
print('5 - linear and quadratic approximation')
print('6 - area of a figure')
print('7 - integral of Lagrange and two approximations')
print('8 - partial derivatives')
print('9 - monotonicity')
print()

number = 0

try:
    number = int(input('Enter a number: '))
    print()
except ValueError as error:
    print(f'You entered something that is not a number: {error}')
else:
    match number:
        case 1:
            create_2d_chart()
        case 2:
            create_3d_chart()
        case 3:
            calc_med_mea_dev()
        case 4:
            lagrange_interpolation()
        case 5:
            create_approximation_charts()
        case 6:
            calculate_figure_area()
        case 7:
            calc_integral_and_approx()
        case 8:
            calc_partial_derivatives()
        case 9:
            calc_monotonicity()
