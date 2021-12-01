import os
import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day01.txt')


class Day01:

    def __init__(self):
        self.inputs = np.loadtxt(INPUT_PATH, dtype=np.int32)

    @staticmethod
    def compute(arr: np.ndarray):
        result = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                result += 1
        return result

    def solve1(self):
        return Day01.compute(self.inputs)

    def solve2(self):
        sums = self.inputs[2:] + self.inputs[1:-1] + self.inputs[:-2]
        return Day01.compute(sums)


def main():
    x = Day01()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
