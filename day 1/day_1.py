from typing import List

def read_input(input_file: str) -> List[int]:
    nums = list()
    with open(input_file) as f:
        for line in f:
            nums.append(int(line.strip()))
    return nums

def part_1(nums: List[int]) -> int:
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
    return count

def part_2(nums: List[int]) -> int:
    count = 0
    sum = 0
    for i in range(len(nums)):
        prev_sum = sum
        sum += nums[i]
        if i > 2:
            sum -= nums[i - 3]
            if sum > prev_sum:
                count += 1
    return count

nums = read_input('input.txt')

print(part_1(nums))

print(part_2(nums))


