import os
from math import ceil, sqrt

import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day17.txt')


class Day17:
    def __init__(self):
        with open(INPUT_PATH, 'r') as infile:
            line = infile.readline().strip()
        seg_x, seg_y = line[len('target area: '):].split(', ')
        self.x0, self.x1 = [int(_) for _ in seg_x[2:].split('..')]
        self.y0, self.y1 = [int(_) for _ in seg_y[2:].split('..')]

    def solve1(self):
        n = abs(self.y0) - 1
        return (n * (n + 1)) // 2

    def solve2(self):
        min_x, max_x = ceil(sqrt(8 * self.x0 + 1) / 2 - 1), self.x1 + 1
        min_y, max_y = self.y0, abs(self.y0)

        xd = np.arange(max_x - min_x) + min_x
        xi = np.arange(len(xd))
        x = np.zeros(xd.shape, dtype=xd.dtype)
        yd = np.arange(max_y - min_y) + min_y
        yi = np.arange(len(yd))
        y = np.zeros(yd.shape, dtype=yd.dtype)

        s_results = set()
        while True:
            # next step
            x += xd
            y += yd
            xd -= 1
            yd -= 1
            xd[xd < 0] = 0
            # trim arrays
            xd = xd[x <= self.x1]
            xi = xi[x <= self.x1]
            x = x[x <= self.x1]
            yd = yd[y >= self.y0]
            yi = yi[y >= self.y0]
            y = y[y >= self.y0]
            # check break condition
            if len(x) == 0 or len(y) == 0:
                break
            # count steps
            for _x in xi[x >= self.x0]:
                for _y in yi[y <= self.y1]:
                    s_results.add((_x, _y))

        return len(s_results)


def main():
    x = Day17()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
