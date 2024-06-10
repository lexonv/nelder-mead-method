import numpy as np
from matplotlib import pyplot as plt
from neldermead import neldermead
from wykresy import wykresy
import funkcje
import ograniczenia

# ===================================================================================================================
# INSTRUKCJA OBSŁUGI PROGRAMU
# 1. Wybierz dla jakiej funkcji wykonujesz optymalizację, punkt początkowy można zmienić przez zmienną x0
# 1 - fun. Rosenbrocka, 2 - fun. Bootha, 3 - fun. Three-hump Camel
ktora_funkcja = 2

if ktora_funkcja == 1:
    x0 = np.array([-5.0, 10.0], dtype=np.float64)
    x1lim = [-5.5, 5.5]
    x2lim = [-3.0, 11]
    fun = funkcje.Rosenbrock()
    funWykres = funkcje.Rosenbrock()
elif ktora_funkcja == 2:
    x0 = np.array([-10.0, 10.0], dtype=np.float64)
    x1lim = [-11, 5.5]
    x2lim = [-3.0, 12]
    fun = funkcje.Booth()
    funWykres = funkcje.Booth()
else:
    x0 = np.array([-5.0, 5.0], dtype=np.float64)
    x1lim = [-5.5, 2.5]
    x2lim = [-2.5, 5.5]
    fun = funkcje.ThreeHump()
    funWykres = funkcje.ThreeHump()

# 2. Czy realizujesz optymalizację z ograniczeniami?
czy_ograniczenia = True
if czy_ograniczenia:
    if ktora_funkcja == 1:
        fun = ograniczenia.RosenbrockOgr(fun, 1e3)
    elif ktora_funkcja == 2:
        fun = ograniczenia.BoothOgr(fun, 1e3)
    else:
        fun = ograniczenia.ThreeHumpOgr(fun, 1e3)

# 3. Aby dobrać odpowiednie parametry algorytmu, należy zmienić poniższe zmienne:
step = 0.1  #Szerokość początkowego simplexa
TolFun = 1e-6  #Dokładność na zbieżność wart. funkcji celu
TolFunCount = 10  #Dopuszczalna ilość spełnienia warunku TolFun pod rząd
max_iter = 300  #Maksymalna ilość iteracji
alpha = 2.0  #Skalar kroku przy odbiciu
gamma = 1.0 #Skalar kroku przy rozszerzeniu
rho = 0.5  #Skalar kroku przy skurczeniu
sigma = 0.5  #Skalar kroku przy zmniejszeniu

# 4. Uruchom program
# ===================================================================================================================

[x_vec, fval, i, t] = neldermead(fun, x0, step, TolFun, TolFunCount, max_iter, alpha, gamma, rho, sigma)

print("---- Znaleziono punkt ----")
print("Minimum: x1 = " + str(round(x_vec[-1, 0], 3)) + ", x2 = " + str(round(x_vec[-1, 1], 3)) + ", f(x1,x2) = " + str(
    round(fval[-1, 0])))
print("Iteracje = " + str(i))
print("Ilość wywołań = " + str(fun.counter))
print("Czas wykonywania programu: " + str(round(t, 3)) + " [s]")

plt.rcParams.update({'font.size': 16})

# Wykres z ograniczeniami (jeżeli są)
fig6 = plt.subplot()
x1 = np.linspace(x1lim[0], x1lim[1], 100)
x2 = np.linspace(x2lim[0], x2lim[1], 100)
X1, X2 = np.meshgrid(x1, x2)
Z = funWykres([X1, X2])
plt.contour(X1, X2, Z, np.linspace(1, 100))
plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='*', linestyle='none', markersize=10, color='orange')
plt.xlabel("X1", fontsize=20)
plt.ylabel("X2", fontsize=20)
plt.title("Wykres konturowy")
plt.xlim(x1lim[0], x1lim[1])
plt.ylim(x2lim[0], x2lim[1])
plt.grid()
if ktora_funkcja == 1 and czy_ograniczenia:
    plt.plot(x1, 1.5 - 0.5 * x1, linestyle='dashed', color='r')
elif ktora_funkcja == 2 and czy_ograniczenia:
    plt.plot(x1, pow(x1, 2.0) + 2 * x1, linestyle='dashed', color='r')
    plt.fill_between(x1, pow(x1, 2.0) + 2 * x1, x2lim[1], color='r', alpha=0.2)
elif ktora_funkcja == 3 and czy_ograniczenia:
    circle = plt.Circle((0.0, 0.0), 1.0, linestyle='dashed', color='r', fill=True, alpha=0.2)
    fig6.add_artist(circle)
plt.show()

wykresy(funWykres, x1lim, x2lim, x_vec, fval)



#Rysowanie ścieżki dla trzech różnych punktów początkowych
# x01 = [-5.0, 5.0]
# x02 = [2.5, 5.0]
# x03 = [-7.5, -5.0]

# x01 = [-5.0, -5.0]
# x02 = [-5.0, -5.0]
# x03 = [-5.0, -5.0]
# #
# #
# TolFun1 = 1e-5
# max_iter1 = 200
#
# TolFun2 = 1e-3
# max_iter2 = 100
#
# TolFun3 = 1e-2
# max_iter3 = 100
# # #
# [x_vec1, f1, i1, t1] = neldermead(fun, x01, step, TolFun1, TolFunCount, max_iter1, alpha, gamma, rho, sigma)
# [x_vec2, f2, i2, t2] = neldermead(fun, x02, step, TolFun2, TolFunCount, max_iter2, alpha, gamma, rho, sigma)
# [x_vec3, f3, i3, t3] = neldermead(fun, x03, step, TolFun3, TolFunCount, max_iter3, alpha, gamma, rho, sigma)
# #
# fig = plt.figure()
# plt.contour(X1, X2, Z, np.linspace(1, 100))
# plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='*', linestyle='none', markersize=10, color='orange')
# plt.xlabel("X1", fontsize=20)
# plt.ylabel("X2", fontsize=20)
# plt.xlim(-6.0, 4.0)
# plt.ylim(-6.0, 8.0)
# plt.grid()
# plt.plot(x01[0], x01[1], marker='*', linestyle='none', markersize=15, color='red')
# plt.plot(x02[0], x02[1], marker='*', linestyle='none', markersize=15, color='magenta')
# plt.plot(x03[0], x03[1], marker='*', linestyle='none', markersize=15, color='green')
# plt.plot(x_vec1[:, 0], x_vec1[:, 1], marker='*', markersize=2, color='r')
# plt.plot(x_vec2[:, 0], x_vec2[:, 1], marker='*', markersize=2, color='magenta')
# plt.plot(x_vec3[:, 0], x_vec3[:, 1], marker='*', markersize=2, color='green')
# plt.show()

# import functools


# def zliczajWywolania(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.funcCount += 1
#         return func(*args, **kwargs)
#
#     wrapper.funcCount = 0
#     return wrapper
#
#
# @zliczajWywolania
# def f1(x):
#     return pow((1 - x[0]), 2) + 100 * pow(x[1] - pow(x[0], 2), 2)
#
#
# @zliczajWywolania
# def f2(x):
#     return pow(x[0] + 2.0 * x[1] - 7.0, 2.0) + pow(2.0 * x[0] + x[1] - 5.0, 2.0)
#
#
# @zliczajWywolania
# def f3(x):
#     return 2.0 * pow(x[0], 2.0) + 1.05 * pow(x[0], 4.0) + pow(x[0], 6.0) / 6.0 + x[0] * x[1] + pow(x[1], 2.0)
#
#
# def ogr1(x):
#     return 1.5 - 0.5 * x[0] - x[1]
#
#
# def ogr2(x):
#     return pow(x[0], 2.0) + 2 * x[0] - x[1]
#
#
# def ogr3(x):
#     return pow(x[0], 2.0) + pow(x[1], 2.0) - 1.0
#
#
# def f1ogr(x):
#     return f1(x) + 1e3 * pow(ogr1(x), 2.0)
#
#
# def f2ogr(x):
#     return f2(x) + 1e3 * max(0.0, pow(ogr2(x), 3.0))
#
#
# def f3ogr(x):
#     return f3(x) + 1e6 * max([0.0, pow(ogr3(x), 3.0)])