import os
from typing import Callable

import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day07.txt')


class Day07:
    def __init__(self):
        self.inputs = np.loadtxt(INPUT_PATH, dtype=np.int32, delimiter=',')

    def _find_lowest_fuel(self, compute_fuel: Callable[[np.ndarray], np.ndarray]):
        lowest_fuel = compute_fuel(np.abs(self.inputs))
        for i in range(1, np.max(self.inputs) + 1):
            fuel = compute_fuel(np.abs(self.inputs - i))
            if fuel >= lowest_fuel:
                break
            lowest_fuel = fuel
        return lowest_fuel

    def solve1(self):
        return self._find_lowest_fuel(lambda x: np.sum(x))

    def solve2(self):
        return self._find_lowest_fuel(lambda x: np.sum((x * (x + 1)) // 2))


def main():
    x = Day07()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
