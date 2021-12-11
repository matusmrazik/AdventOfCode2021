import os
from collections import deque

import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day11.txt')

DIFFS = np.array([[x, y] for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0], dtype=np.int64)


def compute_flashes(octopuses: np.ndarray):  # modifies octopuses!
    octopuses += 1
    q = deque(np.argwhere(octopuses > 9))
    if len(q) == 0:  # no flashes
        return 0
    flashes = np.zeros(octopuses.shape, dtype=bool)
    while len(q) > 0:
        pos = q.popleft()
        if flashes[pos[0], pos[1]]:
            continue
        for d_pos in DIFFS:
            new_pos = pos + d_pos
            if np.any(new_pos < 0) or np.any(new_pos >= octopuses.shape):
                continue
            if flashes[new_pos[0], new_pos[1]]:
                continue
            octopuses[new_pos[0], new_pos[1]] += 1
            if octopuses[new_pos[0], new_pos[1]] > 9:
                q.append(new_pos)
        flashes[pos[0], pos[1]] = 1
    octopuses[flashes] = 0
    return np.count_nonzero(flashes)


class Day11:
    def __init__(self):
        self.inputs = np.genfromtxt(INPUT_PATH, dtype=np.int8, delimiter=1)

    def solve1(self):
        octopuses = self.inputs.copy()
        return sum([compute_flashes(octopuses) for _ in range(100)])

    def solve2(self):
        octopuses = self.inputs.copy()
        step = 1
        while compute_flashes(octopuses) != self.inputs.size:
            step += 1
        return step


def main():
    x = Day11()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
