import numpy as np
import functools
from neldermead import neldermead
from wykresy import wykresy


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


fun = f2
if fun == f1:
    x0 = np.array([-5, 10], dtype=np.float64)
    x1lim = [-5.5, 5.5]
    x2lim = [-3.0, 11]
elif fun == f2:
    x0 = np.array([-10, 10], dtype=np.float64)
    x1lim = [-11, 5.5]
    x2lim = [-3.0, 11]
else:
    x0 = np.array([-5, 5], dtype=np.float64)
    x1lim = [-5.5, 2.5]
    x2lim = [-2.5, 5.5]

step = 0.1
TolFun = 1e-6
TolFunCount = 10
max_iter = 500
alpha = 2.0
gamma = 1.0
rho = 0.5
sigma = 0.5

[x_vec, fval_vec, iteracje]= neldermead(fun, x0, step, TolFun, TolFunCount, max_iter, alpha, gamma, rho, sigma)

print("---- Znaleziono punkt ----")
print("Minimum: x1 = "+str(x_vec[-1, 0])+", x2 = "+str(x_vec[-1, 1])+", f(x1,x2) = "+str(fval_vec[-1, 0]))
print("Iteracje = " + str(iteracje))
print("Ilość wywołań = " + str(fun.funcCount))

wykresy(fun, x1lim, x2lim, x_vec, fval_vec)