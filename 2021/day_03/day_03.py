from typing import List
from collections import defaultdict

class Day_03:
    def read_input(self, file_name: str):
        with open(file_name) as f:
            self.nums = [x.strip() for x in f.readlines()]
        return None

    def part1(self) -> int:
        counts = [0] * len(self.nums[0])
        for i in range(len(self.nums)):
            dgt = list(map(int, list(self.nums[i])))
            for j in range(len(counts)):
                counts[j] += dgt[j]
        gamma = 0
        epsilon = 0
        pow2 = 1 << (len(counts) - 1)
        for j in range(len(counts)):
            if counts[j] > len(self.nums) / 2:
                gamma += pow2
            else:
                epsilon += pow2
            pow2 = pow2 >> 1
        return gamma * epsilon

    def part2(self) -> int:
        nums = self.nums.copy()
        j = 0
        while len(nums) > 1:
            count = 0
            for item in nums:
                if item[j] == '1':
                    count += 1
            if count >= len(nums) / 2:
                ch = '1'
            else:
                ch = '0'
            new_nums = list()
            for item in nums:
                if item[j] == ch:
                    new_nums.append(item)
            nums = new_nums
            j += 1
        oxygen = nums[0]
        nums = self.nums.copy()
        j = 0
        while len(nums) > 1:
            count = 0
            for item in nums:
                if item[j] == '1':
                    count += 1
            if count >= len(nums) / 2:
                ch = '0'
            else:
                ch = '1'
            new_nums = list()
            for item in nums:
                if item[j] == ch:
                    new_nums.append(item)
            nums = new_nums
            j += 1
        CO2 = nums[0]
        return int(oxygen, 2) * int(CO2, 2)




solution = Day_03()

solution.read_input('test.txt')
print(solution.part1())
print(solution.part2())

solution.read_input('input.txt')
print(solution.part1())
print(solution.part2())