

class Counter:
    def __init__(self) -> None:
        self.counter = 0

    def __call__(self):
        self.counter += 1
        return 0


class Rosenbrock(Counter):
    def __init__(self, a=1, b=100) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def __call__(self, x) -> float:
        super().__call__()
        return pow((self.a - x[0]), 2) + self.b * pow(x[1] - pow(x[0], 2), 2)


class Booth(Counter):
    def __call__(self, x) -> float:
        super().__call__()
        return pow(x[0] + 2.0 * x[1] - 7.0, 2.0) + pow(2.0 * x[0] + x[1] - 5.0, 2.0)


class ThreeHump(Counter):
    def __call__(self, x) -> float:
        super().__call__()
        return 2.0 * pow(x[0], 2.0) + 1.05 * pow(x[0], 4.0) + pow(x[0], 6.0) / 6.0 + x[0] * x[1] + pow(x[1], 2.0)



