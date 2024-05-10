import math
import numpy as np
import matplotlib.pyplot as plt
import functools
import copy

def zliczajWywolania(func):
    @functools.wraps(func)
    def wrapper(x1,x2):
        wrapper.funcCount += 1
        return func(x1,x2)
    wrapper.funcCount = 0
    return wrapper

@zliczajWywolania
def f1(x1,x2):
    return pow((1-x1), 2)+1*pow(x2-pow(x1, 2), 2)

@zliczajWywolania
def f2(x1,x2):
    return pow(x1+2*x2+7,2)+pow(2*x1+x2+5,2)

@zliczajWywolania
def f3(x1,x2):
    return 2*x1-1.05*pow(x1,4)+pow(x1,6)/6+x1*x2+pow(x2,2)

def f(x):
    return 2*x[0]-1.05*pow(x[0],4)+pow(x[0],6)/6+x[0]*x[1]+pow(x[1],2)

x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
a = 1
b = 1

X1, X2 = np.meshgrid(x1,x2)
Z = f3(X1,X2)

# plt.contour(X1,X2,Z)
# plt.xlabel('X1')
# plt.ylabel('X2')
# plt.title('Wykres konturowy funkcji')
# plt.plot(1, 1, marker="o", markersize=5)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_surface(X1,X2,Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
# ax.set_xlabel('X1')
# ax.set_ylabel('X2')
# ax.set_zlabel('Z')
# plt.show()


#inicjalizacja, tworzę punkt początkowy x0, f(x0)
x0 = np.array([0., 0.])
f0 = f(x0)
step = 0.6
N = len(x0)
points = [[x0, f0]]

#tworzenie dwóch kolejnych punktów na podstawie punktu początkowego x0, step określa początkową
#odległość punktów od x0
for i in range(N):
    x = copy.copy(x0)
    x[i] = x[i] + step
    val = f(x)
    points.append([x, val])


#sortuj punkty względem f(x) (od min do max), zapisz najlepszy
points.sort(key=lambda x: x[1])
best = points[0][1]


#obliczam centroidę z N-1 punktów (bez ostatniego xn+1)
xo = [0.] * N
for vec in points[:-1]:
    for i, c in enumerate(vec[0]):
        xo[i] = xo[i] + c / (len(points) - 1)


#odbicie, nadpisywane pod warunkiem, że punkt po odbiciu jest lepszy od najgorszego, ale nie najlepszy
alpha = 1.0
xr = xo + alpha * (xo - points[-1][0])
refl_fval = f(xr)
if points[0][1] <= refl_fval < points[-2][1]:
    del points[-1]
    points.append([xr, refl_fval])


#rozszerzenie, wykonaj jeżeli warunek odbicia nie spełnione
#jezeli punkt po odbiciu (xo) jest najlepszy -> przesun go jeszcze dalej
#jeżeli poprawiło -> zastępujemy punkt punktem po rozszerzeniu (xe)
gamma = 1.0
if refl_fval < points[0][1]:
    xe = xo + gamma * (xo - points[-1][0])
    exp_fval = f(xe)
    if exp_fval < refl_fval:
        del points[-1]
        points.append([xe, exp_fval])
    else:
        del points[-1]
        points.append([xr, refl_fval])


#skurczenie, wykonaj jeżeli
rho = 1.0
xc = xo + rho*(x0 - points[-1][0])
cont_fval = f(xc)
if cont_fval < points[-1][1]:
    del points[-1]
    points.append([xc, cont_fval])


#zmniejszenie
sigma = 1.0
x1 = points[0][0]
temp = []
for vec in points:
    xi = x1 + sigma * (vec[0] - x1)
    shrink_fval = f(xi)
    temp.append([xi, shrink_fval])
points = temp