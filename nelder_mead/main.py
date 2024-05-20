import numpy as np
import functools
from matplotlib import pyplot as plt
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
    return pow(x[0] + 2.0 * x[1] - 7.0, 2.0) + pow(2.0 * x[0] + x[1] - 5.0, 2.0)


@zliczajWywolania
def f3(x):
    return 2.0*pow(x[0], 2.0) + 1.05*pow(x[0], 4.0) + pow(x[0], 6.0)/6.0 + x[0]*x[1] + pow(x[1], 2.0)


def ogr1(x):
    return 1.5 - 0.5*x[0] - x[1]


def ogr2(x):
    return pow(x[0], 2.0) + 2*x[0] - x[1]


def ogr3(x):
    return pow(x[0], 2.0) + pow(x[1], 2.0) - 1.0


@zliczajWywolania
def f1ogr(x):
    return f1(x) + 1e3 * pow(ogr1(x), 2.0)


@zliczajWywolania
def f2ogr(x):
    return f2(x) + 1e1 * max(0.0, pow(ogr2(x), 2.0))


@zliczajWywolania
def f3ogr(x):
    return f3(x) + 1e3 * max(0.0, pow(ogr3(x), 2.0))


fun = f3ogr
if fun == f1 or fun == f1ogr:
    x0 = np.array([-5, 10], dtype=np.float64)
    x1lim = [-5.5, 5.5]
    x2lim = [-3.0, 11]
    funWykres = f1
elif fun == f2 or fun == f2ogr:
    x0 = np.array([-10, 10], dtype=np.float64)
    x1lim = [-11, 5.5]
    x2lim = [-3.0, 11]
    funWykres = f2
else:
    x0 = np.array([-5, 5], dtype=np.float64)
    x1lim = [-5.5, 2.5]
    x2lim = [-2.5, 5.5]
    funWykres = f3


step = 0.1
TolFun = 1e-6
TolFunCount = 10
max_iter = 300
alpha = 2.0
gamma = 1.0
rho = 0.5
sigma = 0.5
levels = 20


[x_vec, fval_vec, iteracje] = neldermead(fun, x0, step, TolFun, TolFunCount, max_iter, alpha, gamma, rho, sigma)

print("---- Znaleziono punkt ----")
print("Minimum: x1 = "+str(round(x_vec[-1, 0], 3))+", x2 = "+str(round(x_vec[-1, 1], 3))+", f(x1,x2) = "+str(round(fval_vec[-1, 0], 3)))
print("Iteracje = " + str(iteracje))
print("Ilość wywołań = " + str(fun.funcCount))

# wykresy(funWykres, x1lim, x2lim, x_vec, fval_vec, levels)

# Wykres z ograniczeniami (jeżeli są)
fig6 = plt.figure()
x1 = np.linspace(x1lim[0], x1lim[1], 100)
x2 = np.linspace(x2lim[0], x2lim[1], 100)
X1, X2 = np.meshgrid(x1, x2)
Z = funWykres([X1, X2])
plt.contour(X1, X2, Z, np.linspace(1, 100, levels))
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Wykres konturowy z ograniczeniami")
plt.xlim(x1lim[0], x1lim[1])
plt.ylim(x2lim[0], x2lim[1])
if fun == f1ogr:
    plt.plot(x1, 1.5 - 0.5 * x1, linestyle='dashed', color='r')
    plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='*', linestyle='none', markersize=5)
elif fun == f2ogr:
    plt.plot(x1, pow(x1, 2.0) + 2 * x1, linestyle='dashed', color='r')
    plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='*', linestyle='none', markersize=5)
elif fun == f3ogr:
    plt.plot(x1, np.sqrt(np.fabs(pow(x1, 2.0) - 1.0)), linestyle='dashed', color='r')
    plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='*', linestyle='none', markersize=5)
plt.show()
