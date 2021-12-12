import os
from collections import deque

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day12.txt')


class Day12:
    def __init__(self):
        self.paths: dict[str, set[str]] = dict()
        self.nodes: set[str] = set()
        with open(INPUT_PATH, 'r') as infile:
            for line in infile:
                src, dst = line.strip().split('-')
                self.paths.setdefault(src, set()).add(dst)
                self.paths.setdefault(dst, set()).add(src)
                self.nodes.update({src, dst})

    def solve1(self):
        # visit info of each node, current node name
        q: deque[tuple[dict[str, bool], str]] = deque()
        q.append(({k: False for k in self.nodes}, 'start'))
        result = 0
        while len(q) > 0:
            state, node = q.popleft()
            if node == 'end':
                result += 1
                continue
            d_state = {node: True} if node.islower() else dict()
            for dst_node in self.paths[node]:
                if state[dst_node]:
                    continue
                new_state = state.copy()
                new_state.update(d_state)
                q.append((new_state, dst_node))
        return result

    def solve2(self):
        # visit info of each node, current node name, has visited a node twice
        q: deque[tuple[dict[str, bool], str, bool]] = deque()
        q.append(({k: False for k in self.nodes}, 'start', False))
        result = 0
        while len(q) > 0:
            state, node, visited_twice = q.popleft()
            if node == 'end':
                result += 1
                continue
            d_state = {node: True} if node.islower() else dict()
            for dst_node in self.paths[node]:
                if dst_node == 'start' or (state[dst_node] and visited_twice):
                    continue
                new_state = state.copy()
                new_state.update(d_state)
                new_visited_twice = visited_twice or state[dst_node]
                q.append((new_state, dst_node, new_visited_twice))
        return result


def main():
    x = Day12()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
