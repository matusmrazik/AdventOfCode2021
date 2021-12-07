import os
import numpy as np

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day04.txt')


class Day04:
    def __init__(self):
        self.numbers = np.loadtxt(INPUT_PATH, dtype=np.uint8, delimiter=',', max_rows=1)
        self.boards = np.loadtxt(INPUT_PATH, dtype=np.uint8, skiprows=1).reshape((-1, 5, 5))

    def solve1(self):
        boards_filled = np.zeros(self.boards.shape, dtype=bool)
        board_pos, winning_num = None, None
        for num in self.numbers:
            boards_filled[self.boards == num] = True
            boards_won = np.any(np.all(boards_filled, axis=1) + np.all(boards_filled, axis=2), axis=1)
            if np.any(boards_won):
                board_pos = np.where(boards_won)[0]
                winning_num = num
                break
        return np.sum(self.boards[board_pos] * np.logical_not(boards_filled[board_pos])) * winning_num

    def solve2(self):
        boards_filled = np.zeros(self.boards.shape, dtype=bool)
        board_pos, winning_num = None, None
        prev_losers = np.arange(len(boards_filled))
        for num in self.numbers:
            boards_filled[self.boards == num] = True
            boards_won = np.any(np.all(boards_filled, axis=1) + np.all(boards_filled, axis=2), axis=1)
            if np.all(boards_won):
                board_pos = prev_losers[-1]
                winning_num = num
                break
            prev_losers = np.where(np.logical_not(boards_won))
        return np.sum(self.boards[board_pos] * np.logical_not(boards_filled[board_pos])) * winning_num


def main():
    x = Day04()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
