from typing import List
from collections import defaultdict


class Board:
    def __init__(self, nums: List[List[int]]):
        self.coords = dict()
        self.rows = [set() for x in range(len(nums))]
        self.cols = [set() for x in range(len(nums))]
        self.bingo = False
        self.sum = 0
        for i, line in enumerate(nums):
            for j, dgt in enumerate(line):
                self.coords[dgt] = (i, j)
                self.rows[i].add(dgt)
                self.cols[j].add(dgt)
                self.sum += dgt

    def coords(self, x):
        return self.coords.get(x)

    def remove(self, x):
        if x in self.coords:
            i, j = self.coords[x]
            del self.coords[x]
            self.rows[i].remove(x)
            self.cols[j].remove(x)
            self.sum -= x
            if not self.rows[i] or not self.cols[j]:
                self.bingo = True
                return True
        return False


class Day_04:
    def read_input(self, file_name: str):
        def read_matrix(f):
            matrix = list()
            while True:
                line = f.readline()
                if not line or line == '\n':
                    return matrix if matrix else None
                else:
                    matrix.append(list(map(int, line.strip().split())))

        with open(file_name) as f:
            self.nums = list(map(int, f.readline().strip().split(',')))
            self.boards = list()
            f.readline()
            while True:
                matrix = read_matrix(f)
                if matrix is not None:
                    self.boards.append(Board(matrix))
                else:
                    break

    def part1(self) -> int:
        for num in self.nums:
            for board in self.boards:
                if board.remove(num):
                    return board.sum * num

    def part2(self) -> int:
        for num in self.nums:
            for board in self.boards:
                if not board.bingo and board.remove(num):
                    last_win = board.sum * num
        return last_win





solution = Day_04()

solution.read_input('test.txt')
print(solution.part1())
print(solution.part2())

solution.read_input('input.txt')
print(solution.part1())
print(solution.part2())