import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day02.txt')


def parse_line(line: str):
    items = line.split(' ')
    return items[0], int(items[1])


class Day02:
    def __init__(self):
        with open(INPUT_PATH, 'r') as infile:
            lines = infile.readlines()
        self.inputs = [parse_line(line) for line in lines]

    def solve1(self):
        horizontal, vertical = 0, 0
        for direction, units in self.inputs:
            if direction == 'forward':
                horizontal += units
            elif direction == 'down':
                vertical += units
            elif direction == 'up':
                vertical -= units
        return horizontal * vertical

    def solve2(self):
        horizontal, vertical, aim = 0, 0, 0
        for direction, units in self.inputs:
            if direction == 'forward':
                horizontal += units
                vertical += units * aim
            elif direction == 'down':
                aim += units
            elif direction == 'up':
                aim -= units
        return horizontal * vertical


def main():
    x = Day02()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
