class Counter:
    def __init__(self) -> None:
        self.counter = 0

    def __call__(self):
        self.counter += 1
        return 0


class Ograniczenia(Counter):
    def __init__(self, f, r) -> None:
        super().__init__()
        self.f = f
        self.r = r

    def ogr(self, x) -> float:
        pass

    def __call__(self, x) -> float:
        super().__call__()
        return self.f(x) + self.r * self.ogr(x)


class RosenbrockOgr(Ograniczenia):
    def __init__(self, f, r) -> None:
        super().__init__(f, r)

    def ogr(self, x) -> float:
        return pow(1.5 - 0.5 * x[0] - x[1], 2)


class BoothOgr(Ograniczenia):
    def __init__(self, f, r) -> None:
        super().__init__(f, r)

    def ogr(self, x) -> float:
        return max(0, pow(pow(x[0], 2.0) + 2 * x[0] - x[1], 3))


class ThreeHumpOgr(Ograniczenia):
    def __init__(self, f, r) -> None:
        super().__init__(f, r)

    def ogr(self, x) -> float:
        return pow(pow(x[0], 2.0) + pow(x[1], 2.0) - 1.0, 3)





