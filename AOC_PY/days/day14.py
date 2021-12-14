import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day14.txt')


def increment(d: dict[str, int], key: str, value: int, is_safe=False):
    if is_safe or key in d:
        d[key] += value
    else:
        d[key] = value


def find_min_max(d: dict[str, int]):
    min_elem, max_elem = None, None
    for key, val in d.items():
        if min_elem is None or val < min_elem:
            min_elem = val
        if max_elem is None or val > max_elem:
            max_elem = val
    return min_elem, max_elem


class Day14:
    def __init__(self):
        with open(INPUT_PATH, 'r') as infile:
            self.rules = dict()
            self.initial = infile.readline().strip()
            infile.readline()
            for line in infile:
                pair, in_char = line.strip().split(' -> ')
                self.rules[pair] = in_char

    def _construct_count_dicts(self):
        char_counts, pair_counts = dict(), dict()
        for c in self.initial:
            increment(char_counts, c, 1)
        for i in range(len(self.initial) - 1):
            increment(pair_counts, self.initial[i:i + 2], 1)
        return char_counts, pair_counts

    def _next_step(self, char_counts: dict[str, int], pair_counts: dict[str, int]):
        pair_counts_copy = pair_counts.copy()
        for pair, count in pair_counts_copy.items():
            in_char = self.rules[pair]
            increment(pair_counts, pair, -count, is_safe=True)
            increment(pair_counts, pair[0] + in_char, count)
            increment(pair_counts, in_char + pair[1], count)
            increment(char_counts, in_char, count)

    def solve_general(self, steps: int):
        char_counts, pair_counts = self._construct_count_dicts()
        for _ in range(steps):
            self._next_step(char_counts, pair_counts)
        min_val, max_val = find_min_max(char_counts)
        return max_val - min_val

    def solve1(self):
        return self.solve_general(10)

    def solve2(self):
        return self.solve_general(40)


def main():
    x = Day14()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
