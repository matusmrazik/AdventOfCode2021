import os
import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day06.txt')


def compute_created_fish(x: int, days: int):
    if x < 0 or x > 6:
        raise ValueError(f'Invalid value, only values 0 to 6 are allowed, got {x}')

    arr = np.zeros(days, dtype=np.int64)
    for i in range(x, days, 7):
        arr[i] += 1

    for day in range(days):
        if arr[day] == 0:
            continue
        for i in range(day + 9, days, 7):
            arr[i] += arr[day]

    return np.sum(arr) + 1


class Day06:
    def __init__(self):
        self.inputs = np.loadtxt(INPUT_PATH, dtype=np.int8, delimiter=',')

    def solve1(self):
        days = 80
        reproduce_counts = np.array([compute_created_fish(x, days) for x in range(7)], dtype=np.int64)
        return np.sum(reproduce_counts[self.inputs])

    def solve2(self):
        days = 256
        reproduce_counts = np.array([compute_created_fish(x, days) for x in range(7)], dtype=np.int64)
        return np.sum(reproduce_counts[self.inputs])


def main():
    x = Day06()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
