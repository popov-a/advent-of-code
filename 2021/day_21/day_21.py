from collections import Counter

class Day_21:
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


#solution = Day_21()
#print(solution.part1('input.txt'))
#print(solution.part2('input.txt'))

def part1(filename):
    with open(filename) as f:
        _, s1 = f.readline().strip().split(':')
        _, s2 = f.readline().strip().split(':')
        print(s1, s2)
    s1 = int(s1)
    s2 = int(s2)
    count1 = s1
    count2 = s2
    c1 = True
    cube = 0
    count_cube = 0
    sum1 = 0
    sum2 = 0
    while sum1 < 1000 and sum2 < 1000:
        count_cube += 1
        sum = (cube + 1 - 1) % 100 + 1
        sum += (cube + 2 - 1) % 100 + 1
        sum += (cube + 3 - 1) % 100 + 1
        cube = (cube + 3 - 1) % 100 + 1
        if c1:
            count1 = (count1 + sum - 1) % 10 + 1
            sum1 += count1
            c1 = False
        else:
            count2 = (count2 + sum - 1) % 10 + 1
            sum2 += count2
            c1 = True
    print(count1, count2)
    print(sum1, sum2)
    print(count_cube)
    print(min(sum1, sum2) * count_cube * 3)
    return None

print(part1('test.txt'))
#print(part1('input.txt'))
