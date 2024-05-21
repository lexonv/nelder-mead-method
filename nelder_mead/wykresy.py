import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt


def wykresy(f, x1lim, x2lim, x_vec, fval_vec):
    x1 = np.linspace(x1lim[0], x1lim[1], 100)
    x2 = np.linspace(x2lim[0], x2lim[1], 100)
    X1, X2 = np.meshgrid(x1, x2)
    Z = f([X1, X2])
    N = len(x_vec)
    fval = fval_vec.max(axis=1)
    x1 = x_vec[:, 0]
    x2 = x_vec[:, 1]

    # Działanie algorytmu
    fig1 = plt.figure()
    for i in range(N):
        plt.contour(X1, X2, Z, np.linspace(0, 500, 500))
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.title('Działanie algorytmu Nelder-Meada')
        posxmin = min(x_vec[i, 0], x_vec[i, 2], x_vec[i, 4])
        posxmax = min(x_vec[i, 0], x_vec[i, 2], x_vec[i, 4])
        posymin = max(x_vec[i, 1], x_vec[i, 3], x_vec[i, 5])
        posymax = max(x_vec[i, 1], x_vec[i, 3], x_vec[i, 5])
        plt.xlim(posxmin-0.5, posxmax+0.5)
        plt.ylim(posymin-0.5, posymax+0.5)
        plt.plot([x_vec[i, 0], x_vec[i, 2], x_vec[i, 4], x_vec[i, 0]], [x_vec[i, 1], x_vec[i, 3], x_vec[i, 5], x_vec[i, 1]], color='r', linewidth=2)
        plt.show(block=False)
        plt.pause(0.0001)
        plt.close('all')

    # Zbieżność wartości funkcji celu
    fig2 = plt.figure()
    plt.title('Wykres wartości f(x)')
    plt.plot(np.linspace(0, N - 1, N), fval, marker='*', linestyle='none', markersize=2)
    plt.xlabel('Iteracje')
    plt.ylabel('f(x)')

    # Zbieżność wartości zmiennych decyzyjnych
    fig3 = plt.figure()
    plt.title('Wykres wartości zmiennych decyzyjnych x1 i x2')
    plt.subplot(1, 2, 1)
    plt.plot(np.linspace(0, N - 1, N), x1, marker='*', linestyle='none', markersize=2)
    plt.xlabel('Iteracje')
    plt.ylabel('x1')
    plt.subplot(1, 2, 2)
    plt.plot(np.linspace(0, N - 1, N), x2, marker='*', linestyle='none', markersize=2)
    plt.xlabel('Iteracje')
    plt.ylabel('x2')

    # Wykres konturowy
    fig4 = plt.figure()
    plt.title('Wykres konturowy f(x)')
    plt.contour(X1, X2, Z, np.linspace(1, 100, 10))
    plt.plot(x1, x2, marker='*', markersize=2)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='o', linestyle='none', markersize=10)

    #Wykres przestrzenny
    fig5 = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X1, X2, Z, 200)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Z')
    ax.plot3D(x_vec[-1, 0], x_vec[-1, 1], f([x_vec[-1, 0], x_vec[-1, 1]]), marker='o', linestyle='none', markersize=10)

    plt.show()
