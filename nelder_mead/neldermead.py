import numpy as np
import copy

def neldermead(f,x0,step,alpha):

    f0 = f(x0)
    dim = len(x0)
    simplex = [[x0, f0]]

    for i in range(dim):
        x = copy.copy(x0)
        x[i] = x[i] + step
        val = f(x)
        simplex.append([x, val])

    # sortuj punkty
    simplex.sort(key=lambda x: x[1])
    best = simplex[0][1]

    # centroida
    xo = [0.] * dim

    for vec in simplex[:-1]:
        for i, c in enumerate(vec[0]):
            xo[i] = xo[i] + c / (len(simplex) - 1)

    # odbicie
    alpha = 1.0
    xr = xo + alpha * (xo - simplex[-1][0])
    refl_fval = f(xr)
    if simplex[0][1] <= refl_fval < simplex[-2][1]:
        del simplex[-1]
        simplex.append([xr, refl_fval])

    # rozszerzenie
    gamma = 1.0
    if refl_fval < simplex[0][1]:
        xe = xo + gamma * (xo - simplex[-1][0])
        exp_fval = f(xe)
        if exp_fval < refl_fval:
            del simplex[-1]
            simplex.append([xe, exp_fval])
        else:
            del simplex[-1]
            simplex.append([xr, refl_fval])

