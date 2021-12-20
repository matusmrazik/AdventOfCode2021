import os
from typing import Union

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day18.txt')


class Node:
    def __init__(self, value: Union[int, list], parent=None):
        self.parent = parent
        if type(value) is list:
            self.value = None
            self.left, self.right = Node(value[0], parent=self), Node(value[1], parent=self)
        else:
            self.value = value
            self.left, self.right = None, None

    @property
    def is_root(self):
        return self.parent is None

    @property
    def is_leaf(self):
        return self.value is not None

    @property
    def is_left(self):
        return self.parent.left is self

    @property
    def is_right(self):
        return self.parent.right is self

    def __repr__(self):
        return repr(self.value) if self.is_leaf else repr([self.left, self.right])

    def _find_closest_left(self):
        curr = self
        while not curr.is_root and curr.is_left:
            curr = curr.parent
        if curr.is_root:
            return None
        curr = curr.parent.left
        while not curr.is_leaf:
            curr = curr.right
        return curr

    def _find_closest_right(self):
        curr = self
        while not curr.is_root and curr.is_right:
            curr = curr.parent
        if curr.is_root:
            return None
        curr = curr.parent.right
        while not curr.is_leaf:
            curr = curr.left
        return curr

    def _explode(self):
        left = self._find_closest_left()
        if left is not None:
            left.value += self.left.value
        right = self._find_closest_right()
        if right is not None:
            right.value += self.right.value
        self.value = 0
        self.left = None
        self.right = None

    def explode(self, depth=0):
        if self.is_leaf:
            return 0
        if depth < 4:
            if self.left.explode(depth + 1):
                return 1
            return self.right.explode(depth + 1)

        self._explode()
        return 1

    def split(self):
        if not self.is_leaf:
            if self.left.split():
                return 1
            return self.right.split()
        if self.value < 10:
            return 0
        self.left = Node(self.value // 2, parent=self)
        self.right = Node(self.value - self.left.value, parent=self)
        self.value = None
        return 1

    def magnitude(self):
        return self.value if self.is_leaf else 3 * self.left.magnitude() + 2 * self.right.magnitude()


class SnailFishNumber:
    def __init__(self, value: str = None):
        self.root = None if value is None else Node(eval(value))

    def __repr__(self):
        return '' if self.root is None else repr(self.root)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, other):
        result = SnailFishNumber(repr([self, other]))
        result._reduce()
        return result

    def _reduce(self):
        if self.root is None:
            return
        while True:
            explodes = 0
            while True:
                x = self.root.explode()
                explodes += x
                if x == 0:
                    break
            splits = self.root.split()
            if explodes == 0 and splits == 0:
                break

    def magnitude(self):
        return 0 if self.root is None else self.root.magnitude()


class Day18:
    def __init__(self):
        with open(INPUT_PATH, 'r') as infile:
            self.inputs = [SnailFishNumber(_.strip()) for _ in infile]

    def solve1(self):
        a = self.inputs[0]
        for x in self.inputs[1:]:
            a = a + x
        return a.magnitude()

    def solve2(self):
        result = 0
        for i in range(len(self.inputs)):
            for j in range(i + 1, len(self.inputs)):
                sum1 = self.inputs[i] + self.inputs[j]
                sum2 = self.inputs[j] + self.inputs[i]
                result = max(result, sum1.magnitude(), sum2.magnitude())
        return result


def main():
    x = Day18()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
