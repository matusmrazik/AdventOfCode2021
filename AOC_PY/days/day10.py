import os
from collections import deque

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day10.txt')


def analyze_line(line: str):
    stack = deque()  # wait, what? :D
    for char in line:
        if char in '({[<':
            stack.append(char)
            continue
        if len(stack) == 0:
            return char, None
        opening = stack.pop()
        if opening + char not in ('()', '[]', '{}', '<>'):
            return char, None
    return None, stack


def find_illegal_char(line: str):
    illegal_char, _ = analyze_line(line)
    return illegal_char


def find_completion_string(line: str):
    closes = {'(': ')', '[': ']', '{': '}', '<': '>'}
    _, stack = analyze_line(line)
    if stack is None or len(stack) == 0:
        return None
    return ''.join(closes[c] for c in reversed(stack))


class Day10:
    def __init__(self):
        with open(INPUT_PATH) as infile:
            self.inputs = [line.rstrip() for line in infile.readlines()]

    def solve1(self):
        scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

        result = 0
        for line in self.inputs:
            illegal_char = find_illegal_char(line)
            if illegal_char:
                result += scores[illegal_char]

        return result

    def solve2(self):
        scores = {')': 1, ']': 2, '}': 3, '>': 4}

        results = []
        for line in self.inputs:
            completion_string = find_completion_string(line)
            if completion_string:
                points = 0
                for c in completion_string:
                    points = 5 * points + scores[c]
                results.append(points)

        return sorted(results)[len(results) // 2]


def main():
    x = Day10()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
