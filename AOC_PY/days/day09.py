import os
from collections import deque

import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day09.txt')


class Day09:
    def __init__(self):
        self.inputs = np.genfromtxt(INPUT_PATH, dtype=np.int8, delimiter=1)

    def _find_low_points(self):
        m_left = np.ones(self.inputs.shape, dtype=self.inputs.dtype) * 10
        m_left[:, :-1] = self.inputs[:, 1:]
        m_right = np.ones(self.inputs.shape, dtype=self.inputs.dtype) * 10
        m_right[:, 1:] = self.inputs[:, :-1]
        m_up = np.ones(self.inputs.shape, dtype=self.inputs.dtype) * 10
        m_up[:-1] = self.inputs[1:]
        m_down = np.ones(self.inputs.shape, dtype=self.inputs.dtype) * 10
        m_down[1:] = self.inputs[:-1]
        return np.logical_and(
            np.logical_and(self.inputs < m_left, self.inputs < m_right),
            np.logical_and(self.inputs < m_up, self.inputs < m_down)
        )

    def _compute_basin_size(self, pos: np.ndarray):
        basin = np.zeros(self.inputs.shape, dtype=bool)

        q = deque()
        q.append(pos)
        while len(q):
            row, col = q.popleft()
            if basin[row, col]:
                continue
            for d_row, d_col in (1, 0), (0, 1), (-1, 0), (0, -1):
                new_row, new_col = row + d_row, col + d_col
                if new_row < 0 or new_row >= self.inputs.shape[0] or new_col < 0 or new_col >= self.inputs.shape[1]:
                    continue
                if self.inputs[new_row, new_col] == 9 or self.inputs[new_row, new_col] <= self.inputs[row, col]:
                    continue
                q.append((new_row, new_col))
            basin[row, col] = 1

        return np.count_nonzero(basin)

    def solve1(self):
        lows = self._find_low_points()
        return np.sum(self.inputs[lows] + 1)

    def solve2(self):
        lows = self._find_low_points()
        largest_sizes = [0, 0, 0]  # sorted, lowest is first
        for pos in np.argwhere(lows):
            basin_size = self._compute_basin_size(pos)
            if basin_size <= largest_sizes[0]:
                continue
            largest_sizes = sorted(largest_sizes + [basin_size])[1:]
        return np.prod(largest_sizes)


def main():
    x = Day09()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
