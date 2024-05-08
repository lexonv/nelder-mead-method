import math
import numpy as np
import matplotlib.pyplot as plt
import functools

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

x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
a = 1
b = 1

X1, X2 = np.meshgrid(x1,x2)
Z = f3(X1,X2)

plt.contour(X1,X2,Z)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Wykres konturowy funkcji')
plt.plot(1, 1, marker="o", markersize=5)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X1,X2,Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Z')
plt.show()

print(f2.funcCount)