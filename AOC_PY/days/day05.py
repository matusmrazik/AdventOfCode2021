import os
import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day05.txt')


class Day05:
    def __init__(self):
        with open(INPUT_PATH, 'r') as infile:
            lines = infile.readlines()
        self.lines = np.zeros((len(lines), 2, 2), dtype=np.int32)
        for i, line in enumerate(lines):
            p_start, p_end = line.split(' -> ')
            self.lines[i, 0] = np.fromstring(p_start, dtype=self.lines.dtype, sep=',')
            self.lines[i, 1] = np.fromstring(p_end, dtype=self.lines.dtype, sep=',')

    def solve1(self):
        horizontals = self.lines[self.lines[:, 0, 1] == self.lines[:, 1, 1]]
        verticals = self.lines[self.lines[:, 0, 0] == self.lines[:, 1, 0]]

        max_coord = np.max(self.lines) + 1
        board = np.zeros((max_coord, max_coord), dtype=np.int32)

        for h in horizontals:
            xs, y = np.sort(h[:, 0]), h[0, 1]
            board[y, xs[0]:xs[1] + 1] += 1
        for v in verticals:
            x, ys = v[0, 0], np.sort(v[:, 1])
            board[ys[0]:ys[1] + 1, x] += 1

        return np.count_nonzero(board > 1)

    def solve2(self):
        are_horizontals = np.equal(self.lines[:, 0, 1], self.lines[:, 1, 1])
        are_verticals = np.equal(self.lines[:, 0, 0], self.lines[:, 1, 0])

        max_coord = np.max(self.lines) + 1
        board = np.zeros((max_coord, max_coord), dtype=np.int32)

        for i in range(len(self.lines)):
            if are_horizontals[i]:
                xs, y = np.sort(self.lines[i, :, 0]), self.lines[i, 0, 1]
                board[y, xs[0]:xs[1] + 1] += 1
            elif are_verticals[i]:
                x, ys = self.lines[i, 0, 0], np.sort(self.lines[i, :, 1])
                board[ys[0]:ys[1] + 1, x] += 1
            elif (self.lines[i, 0, 0] + self.lines[i, 1, 1]) == (self.lines[i, 1, 0] + self.lines[i, 0, 1]):
                # diagonal, k = 1
                xs, ys = np.sort(self.lines[i, :, 0]), np.sort(self.lines[i, :, 1])
                for x, y in zip(range(xs[0], xs[1] + 1), range(ys[0], ys[1] + 1)):
                    board[y, x] += 1
            else:
                # diagonal, k = -1
                xs, ys = np.sort(self.lines[i, :, 0]), np.sort(self.lines[i, :, 1])
                for x, y in zip(range(xs[0], xs[1] + 1), range(ys[1], ys[0] - 1, -1)):
                    board[y, x] += 1

        return np.count_nonzero(board > 1)


def main():
    x = Day05()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
