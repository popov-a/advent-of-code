from collections import Counter

class Day_07:
    def part1(self, file_name: str) -> int:
        nums = [int(x) for x in open(file_name).readline().strip().split(',')]
        nums.sort()
        center = nums[len(nums) // 2]
        cost = 0
        for item in nums:
            cost += abs(center - item)
        return cost


    def part2(self, file_name: str) -> int:
        def sum3(x: int) -> int:
            return sum(abs(x - item) * (abs(x - item) + 1) // 2 for item in nums)

        nums = [int(x) for x in open(file_name).readline().strip().split(',')]
        min_sum = 1e100
        for x in range(min(nums), max(nums) + 1):
            my_sum = sum3(x)
            if my_sum < min_sum:
                min_sum = my_sum
                print(x)
        return min_sum


solution = Day_07()
#print(solution.part1('test.txt'))
#print(solution.part1('input.txt'))
print(solution.part2('test.txt'))
print(solution.part2('input.txt'))

nums = sorted([int(x) for x in open('input.txt').readline().strip().split(',')])
print(sum(nums) / len(nums))
x = sum(nums) // len(nums)
print(sum(abs(x - item) * (abs(x - item) + 1) // 2 for item in nums))
#print(sorted([int(x) for x in open('test.txt').readline().strip().split(',')]))