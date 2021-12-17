import os
from queue import PriorityQueue

import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day15.txt')


def extend_array(arr: np.ndarray, n: int):
    rows, cols = arr.shape
    new_rows, new_cols = rows * n, cols * n
    new_arr = np.zeros((new_rows, new_cols), arr.dtype)
    new_arr[:rows, :cols] = arr
    for r in range(rows, new_rows, rows):
        chunk = new_arr[r - rows:r, :cols] + 1
        chunk[chunk > 9] = 1
        new_arr[r:r + rows, :cols] = chunk
    for r in range(0, new_rows, rows):
        for c in range(cols, new_cols, cols):
            chunk = new_arr[r:r + rows, c - cols:c] + 1
            chunk[chunk > 9] = 1
            new_arr[r:r + rows, c:c + cols] = chunk
    return new_arr


def find_lowest_path(arr: np.ndarray):
    diffs = (0, 1), (1, 0), (0, -1), (-1, 0)
    max_val = 10 * arr.size
    cache = np.ones(arr.shape, dtype=np.int64) * max_val
    cache[0, 0] = 0
    q = PriorityQueue()
    q.put(QueueItem((0, 0)))
    while not q.empty():
        row, col = q.get().value
        for d_row, d_col in diffs:
            new_row, new_col = row + d_row, col + d_col
            if new_row < 0 or new_col < 0 or new_row >= arr.shape[0] or new_col >= arr.shape[1]:
                continue
            val = cache[row, col] + arr[new_row, new_col]
            if val < cache[new_row, new_col]:
                cache[new_row, new_col] = val
                q.put(QueueItem((new_row, new_col), priority=val))
    return cache[-1, -1]


class QueueItem:
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class Day15:
    def __init__(self):
        self.inputs = np.genfromtxt(INPUT_PATH, dtype=np.int64, delimiter=1)

    def solve1(self):
        return find_lowest_path(self.inputs)

    def solve2(self):
        full_map = extend_array(self.inputs, 5)
        return find_lowest_path(full_map)


def main():
    x = Day15()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
