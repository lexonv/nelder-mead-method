import matplotlib
from animacja import animacja
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")


def wykresy(f, x1lim, x2lim, x_vec, fval_vec):
    x1 = np.linspace(x1lim[0], x1lim[1], 100)
    x2 = np.linspace(x2lim[0], x2lim[1], 100)
    X1, X2 = np.meshgrid(x1, x2)
    Z = f([X1, X2])
    N = len(x_vec)
    fval = fval_vec.max(axis=1)
    x1 = x_vec[:, 0]
    x2 = x_vec[:, 1]

    # Zbieżność wartości funkcji celu
    fig2 = plt.figure()
    plt.title('Wykres wartości f(x)')
    plt.plot(np.linspace(0, N - 1, N), fval, marker='*', linestyle='none', markersize=3, color='red')
    plt.xlabel('Iteracje')
    plt.ylabel('f(x)')
    plt.grid()

    # Zbieżność wartości zmiennych decyzyjnych
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.title("Wykres x1")
    plt.plot(np.linspace(0, N - 1, N), x1, marker='*', linestyle='none', markersize=3, color='red')
    plt.xlabel('Iteracje')
    plt.ylabel('x1')
    plt.grid()
    plt.subplot(1, 2, 2)
    plt.title("Wykres x2")
    plt.plot(np.linspace(0, N - 1, N), x2, marker='*', linestyle='none', markersize=3,color='red')
    plt.xlabel('Iteracje')
    plt.ylabel('x2')
    plt.grid()
    plt.show()

    # Wykres konturowy
    fig4 = plt.figure()
    plt.title('Wykres konturowy f(x)')
    plt.contour(X1, X2, Z, np.linspace(1, 100, 10))
    plt.plot(x1, x2, marker='*', markersize=2, color='r')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='*', color='orange', linestyle='none', markersize=10)
    plt.grid()

    #Wykres przestrzenny
    fig5 = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X1, X2, Z, 200)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')
    ax.plot3D(x_vec[-1, 0], x_vec[-1, 1], f([x_vec[-1, 0], x_vec[-1, 1]]), marker='*', color='orange', linestyle='none', markersize=10)
    plt.show()

    #Animacja
    animacja(f, x_vec, x1lim, x2lim)
