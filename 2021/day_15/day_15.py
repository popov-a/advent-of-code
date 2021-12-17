from typing import List
from collections import defaultdict

class Day_15:
    def read_input(self, file_name: str):
        with open(file_name) as f:
            self.nums = [x.strip() for x in f.readlines()]
        return None

    def part1(self) -> int:
        count = [len(self.nums[0] * 10)] * len(self.nums[0])
        count[0] = -int(self.nums[0][0])
        for item in self.nums:
            count[0] += int(item[0])
            for j in range(1, len(item)):
                count[j] = min(count[j - 1], count[j]) + int(item[j])
        return count[-1]


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




solution = Day_15()

solution.read_input('test.txt')
print(solution.part1())
#print(solution.part2())

solution.read_input('input.txt')
print(solution.part1())
#print(solution.part2())