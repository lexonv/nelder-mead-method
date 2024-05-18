import numpy as np
import matplotlib.pyplot as plt
import functools
import copy

from neldermead import neldermead


def zliczajWywolania(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.funcCount += 1
        return func(*args, **kwargs)

    wrapper.funcCount = 0
    return wrapper


@zliczajWywolania
def f1(x):
    return pow((1 - x[0]), 2) + 100 * pow(x[1] - pow(x[0], 2), 2)


@zliczajWywolania
def f2(x):
    return pow(x[0] + 2 * x[1] - 7, 2) + pow(2 * x[0] + x[1] - 5, 2)


@zliczajWywolania
def f3(x):
    return 2 * x[0] - 1.05 * pow(x[0], 4) + pow(x[0], 6) / 6 + x[0] * x[1] + pow(x[1], 2)


# x1 = np.linspace(-5, 5, 100)
# x2 = np.linspace(-5, 5, 100)
#
# X1, X2 = np.meshgrid(x1,x2)
# Z = f2([X1,X2])
#
# plt.contour(X1,X2,Z)
# plt.xlabel('X1')
# plt.ylabel('X2')
# plt.title('Wykres konturowy funkcji')
# plt.plot(1, 1, marker="o", markersize=5)
#
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_surface(X1,X2,Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
# ax.set_xlabel('X1')
# ax.set_ylabel('X2')
# ax.set_zlabel('Z')
# plt.show()

x0 = np.array([-5.0, 5.0])
step = 1.0
TolFun = 1e-6
TolFunCount = 10
max_iter = 1000
alpha = 1.
gamma = 2.
rho = 0.5
sigma = 0.5

[x_vec, fval_vec, iteracje]= neldermead(f2, x0, step, TolFun, TolFunCount, max_iter, alpha, gamma, rho, sigma)

print("MACIERZ ROZWIĄZAŃ X")
print(x_vec)
print("\n")
print("MACIERZ FVAL")
print(fval_vec)
