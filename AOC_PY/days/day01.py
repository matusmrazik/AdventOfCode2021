import os
import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day01.txt')


class Day01:

    def __init__(self):
        self.inputs = np.loadtxt(INPUT_PATH, dtype=np.int32)

    def solve1(self):
        return self.solve_general()

    def solve2(self):
        return self.solve_general(3)

    def solve_general(self, window=1):
        """Optimized general solution"""
        if window < 1:
            raise ValueError(f'Invalid value for "window", allowed values are positive integers, got {window}')
        return np.count_nonzero(self.inputs[window:] > self.inputs[:-window])


def main():
    x = Day01()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
