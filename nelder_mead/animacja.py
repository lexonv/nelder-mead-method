import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import PillowWriter


def animacja(fun, x_vec, x1lim, x2lim):
    x1 = np.linspace(x1lim[0], x1lim[1], 100)
    x2 = np.linspace(x2lim[0], x2lim[1], 100)
    X1, X2 = np.meshgrid(x1, x2)
    Z = fun([X1, X2])

    fig, ax = plt.subplots()

    def animate(i):
        ax.clear()
        plt.contour(X1, X2, Z, np.linspace(1, 100, 10))
        p1 = x_vec[i, 0]
        p2 = x_vec[i, 1]
        p3 = x_vec[i, 2]
        p4 = x_vec[i, 3]
        p5 = x_vec[i, 4]
        p6 = x_vec[i, 5]
        ax.plot([p1, p3, p5, p1], [p2, p4, p6, p2], color='r')
        plt.plot(x_vec[-1, 0], x_vec[-1, 1], marker='*', linestyle='none', markersize=10, color='orange')
        ax.set_xlabel('X1')
        ax.set_ylabel('X2')
        ax.set_title('Animacja algorytmu Neldera-Meada')
        ax.set_xlim(x1lim)
        ax.set_ylim(x2lim)
        ax.grid()

    anim = animation.FuncAnimation(fig=fig, func=animate, frames=len(x_vec), interval=200)
    # Save the animation as an animated GIF
    # anim.save("przebieg.gif", dpi=300,
    #          writer=PillowWriter(fps=5))
    plt.show()
