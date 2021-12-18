from typing import List
from collections import Counter

class Day_06:
    def part1(self, file_name: str) -> int:
        with open(file_name) as f:
            nums = list(map(int, f.readline().strip().split(',')))
        fishs = dict(Counter(nums))
        for i in range(80):
            fishs_0 = fishs.get(0, 0)
            for j in range(0, 9):
                fishs[j] = fishs.get(j + 1, 0)
            fishs[8] = fishs_0
            fishs[6] = fishs.get(6, 0) + fishs_0
        return sum(fishs.values())


    def part2(self, file_name: str) -> int:
        with open(file_name) as f:
            nums = list(map(int, f.readline().strip().split(',')))
        fishs = dict(Counter(nums))
        for i in range(256):
            fishs_0 = fishs.get(0, 0)
            for j in range(0, 9):
                fishs[j] = fishs.get(j + 1, 0)
            fishs[8] = fishs_0
            fishs[6] = fishs.get(6, 0) + fishs_0
        return sum(fishs.values())


solution = Day_06()
print(solution.part1('input.txt'))
print(solution.part2('input.txt'))