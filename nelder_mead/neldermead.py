import numpy as np
import copy
import time


def neldermead(f, x0, step, TolFun, TolFunCount, max_iter, alpha, gamma, rho, sigma):

    #INICJALIZACJA
    # tworzenie dwóch kolejnych punktów na podstawie punktu początkowego x0, step określa początkową
    # odległość punktów od x0
    f0 = f(x0)
    N = len(x0)
    points = [[x0, f0]]
    prevBEST = f0
    start = time.time()

    for i in range(N):
        x = copy.copy(x0)
        x[i] = x[i] + step
        val = f(x)
        points.append([x, val])

    x_vec = np.linspace(0, 0, len(x0)*3)
    fval_vec = np.linspace(0, 0, 3)
    print("INICJALIZACJA - DONE")
    print("points = " + str(points) + "\n")

    #PETLA GŁÓWNA PROGRAMU
    iter = 0
    noImprovCounter = 0
    while True:

        #Sortuj
        points.sort(key=lambda x: x[1])
        best = points[0][1]

        #Rozszerz wyniki
        x_vec = np.vstack([x_vec, [points[0][0][0], points[0][0][1], points[1][0][0], points[1][0][1], points[2][0][0], points[2][0][1]]])
        fval_vec = np.vstack([fval_vec, [points[0][1], points[1][1], points[1][1]]])

        #Sprawdź warunki stopu
        if iter >= max_iter:
            print("ZADZIAŁAŁ STOP MAX ITER\n")
            end = time.time()
            t = end - start
            return [x_vec[1:, :], fval_vec[1:, :], iter, t]
        iter += 1

        if TolFun < np.fabs(prevBEST - best):
            noImprovCounter = 0
            prevBEST = best
        else:
            noImprovCounter += 1

        if noImprovCounter >= TolFunCount:
            print("ZADZIAŁAŁ STOP NO IMPROVEMENT FVAL\n")
            end = time.time()
            t = end - start
            return [x_vec[1:, :], fval_vec[1:, :], iter, t]



        #OPERACJE ALGORYTMU NELDER-MEAD
        #1) znalezienie centroidy
        #2) odbicie
        #3) rozszerzenie
        #4) skurczenie
        #5) zmniejszenie

        # Centroida
        xo = [0.] * N
        for vec in points[:-1]:
            for i, c in enumerate(vec[0]):
                xo[i] = xo[i] + c / (len(points) - 1)

        # Odbicie
        # nadpisywane pod warunkiem, że punkt po odbiciu jest lepszy od najgorszego, ale nie najlepszy
        xr = xo + alpha * (xo - np.array(points[-1][0]))
        refl_fval = f(xr)
        if points[0][1] <= refl_fval < points[-2][1]:
            del points[-1]
            points.append([xr, refl_fval])
            continue

        # Rozszerzenie
        # wykonaj jeżeli warunek odbicia nie spełniony
        # jezeli punkt po odbiciu (xo) jest najlepszy -> przesun go jeszcze dalej
        # jeżeli poprawiło -> zastępujemy punkt punktem po rozszerzeniu (xe)
        if refl_fval < points[0][1]:
            xe = xo + gamma * (xo - np.array(points[-1][0]))
            exp_fval = f(xe)
            if exp_fval < refl_fval:
                del points[-1]
                points.append([xe, exp_fval])
                continue
            else:
                del points[-1]
                points.append([xr, refl_fval])
                continue

        # Skurczenie
        # podmień jeżeli punkt po skruczeniu jest lepszy od najgorszego
        xc = xo + rho * (x0 - np.array(points[-1][0]))
        cont_fval = f(xc)
        if cont_fval < points[-1][1]:
            del points[-1]
            points.append([xc, cont_fval])
            continue

        # Zmniejszenie
        x1 = points[0][0]
        temp = []
        for vec in points:
            xi = x1 + sigma * (vec[0] - x1)
            shrink_fval = f(xi)
            temp.append([xi, shrink_fval])
        points = temp
