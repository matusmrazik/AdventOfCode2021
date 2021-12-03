import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day03.txt')


def compute_bit_counts(inputs: list[str], position: int = None):
    item_size = len(inputs[0])

    if position is None:
        counts = [0 for _ in range(item_size)], [0 for _ in range(item_size)]
        for item in inputs:
            for i, c in enumerate(item):
                if c == '0':
                    counts[0][i] += 1
                else:
                    counts[1][i] += 1
        return counts

    if position >= item_size or position < 0:
        raise ValueError('Invalid position value')

    c0, c1 = 0, 0
    for item in inputs:
        if item[position] == '0':
            c0 += 1
        else:
            c1 += 1
    return c0, c1


class Day03:
    def __init__(self):
        with open(INPUT_PATH, 'r') as infile:
            lines = infile.readlines()
        self.inputs = [line.strip() for line in lines]

    def solve1(self):
        count_0s, count_1s = compute_bit_counts(self.inputs)

        gamma = ''.join('1' if c1 >= c0 else '0' for c0, c1 in zip(count_0s, count_1s))
        epsilon = ''.join('1' if c0 >= c1 else '0' for c0, c1 in zip(count_0s, count_1s))

        gamma_rate = int(gamma, base=2)
        epsilon_rate = int(epsilon, base=2)

        return gamma_rate * epsilon_rate

    def solve2(self):
        oxygen_items, oxygen_position = self.inputs, 0
        while len(oxygen_items) != 1:
            c0, c1 = compute_bit_counts(oxygen_items, oxygen_position)
            more_common = '1' if c1 >= c0 else '0'
            oxygen_items = [item for item in oxygen_items if item[oxygen_position] == more_common]
            oxygen_position += 1

        co2_items, co2_position = self.inputs, 0
        while len(co2_items) != 1:
            c0, c1 = compute_bit_counts(co2_items, co2_position)
            less_common = '0' if c0 <= c1 else '1'
            co2_items = [item for item in co2_items if item[co2_position] == less_common]
            co2_position += 1

        oxygen_rating = int(oxygen_items[0], base=2)
        co2_rating = int(co2_items[0], base=2)

        return oxygen_rating * co2_rating


def main():
    x = Day03()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
