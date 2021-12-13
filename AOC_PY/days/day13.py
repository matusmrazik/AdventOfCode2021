import os

import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day13.txt')


def fold_paper(paper: np.ndarray, axis: str, position: int):
    rows, cols = paper.shape
    if axis == 'y':
        folded_rows = max(position, rows - position - 1)
        folded = np.zeros((folded_rows, cols), dtype=paper.dtype)
        folded[folded_rows - position:] = paper[:position]
        folded[folded_rows - rows + position + 1:] += paper[rows - 1:position:-1]
        return folded
    folded_cols = max(position, cols - position - 1)
    folded = np.zeros((rows, folded_cols), dtype=paper.dtype)
    folded[:, folded_cols - position:] = paper[:, :position]
    folded[:, folded_cols - cols + position + 1:] += paper[:, cols - 1:position:-1]
    return folded


def paper_to_string(paper: np.ndarray):
    lines = []
    for row in paper:
        line = ''.join(['#' if _ else ' ' for _ in row])
        lines.append(line)
    return '\n'.join(lines)


class Day13:
    def __init__(self):
        self.folds = []
        with open(INPUT_PATH, 'r') as infile:
            marks = []
            for line in infile:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line.startswith('fold along '):
                    axis, pos = line[11:].split('=')
                    self.folds.append((axis, int(pos)))
                else:
                    x_pos, y_pos = line.split(',')
                    marks.append((int(y_pos), int(x_pos)))
        self.marks = np.array(marks)

    def _construct_paper(self):
        paper = np.zeros(np.max(self.marks, axis=0) + 1, dtype=bool)
        paper[self.marks[:, 0], self.marks[:, 1]] = True
        return paper

    def solve1(self):
        paper = self._construct_paper()
        axis, pos = self.folds[0]
        return np.count_nonzero(fold_paper(paper, axis, pos))

    def solve2(self):
        paper = self._construct_paper()
        for fold in self.folds:
            axis, pos = fold
            paper = fold_paper(paper, axis, pos)
        return paper_to_string(paper)


def main():
    x = Day13()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
