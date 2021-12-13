from typing import List

class Day_01:
    def read_input(self, file_name: str):
        with open(file_name) as f:
            self.nums = [int(x.strip()) for x in f.readlines()]
        return None

    def part1(self) -> int:
        count = 0
        for i in range(1, len(self.nums)):
            if self.nums[i] > self.nums[i - 1]:
                count += 1
        return count

    def part2(self) -> int:
        count = 0
        sum = 0
        for i in range(len(self.nums)):
            prev_sum = sum
            sum += self.nums[i]
            if i > 2:
                sum -= self.nums[i - 3]
                if sum > prev_sum:
                    count += 1
        return count

solution = Day_01()

solution.read_input('test.txt')
print(solution.part1())
print(solution.part2())

solution.read_input('input.txt')
print(solution.part1())
print(solution.part2())

