from collections import defaultdict


def part1(file_name: str) -> int:
    count = 0
    with open(file_name) as f:
        for line in f:
            _, data = line.strip().split('|')
            nums = data.split()
            for num in nums:
                if len(num) in [2, 3, 4, 7]:
                    count += 1
            # count += len(list(filter(lambda x: len(x) in [2, 3, 4, 7], nums)))
    return count


def part2(file_name: str) -> int:
    sum = 0
    with open(file_name) as f:
        for line in f:
            digits = defaultdict(set)
            l, r = line.strip().split('|')
            l = l.split()
            r = r.split()
            for num in l:
                if len(num) == 7:
                    digits[8] = set(num)
                elif len(num) == 4:
                    digits[4] = set(num)
                elif len(num) == 3:
                    digits[7] = set(num)
                elif len(num) == 2:
                    digits[1] = set(num)
            for num in l:
                if len(num) == 6:
                    if digits[4].issubset(set(num)):
                        digits[9] = set(num)
                    else:
                        if digits[1].issubset(set(num)):
                            digits[0] = set(num)
                        else:
                            digits[6] = set(num)
            for num in l:
                if len(num) == 5:
                    if digits[1].issubset(set(num)):
                        digits[3] = set(num)
                    else:
                        if set(num).issubset(digits[6]):
                            digits[5] = set(num)
                        else:
                            digits[2] = set(num)
            ans = 0
            for num in r:
                for i in range(10):
                    if digits[i] == set(num):
                        ans = ans * 10 + i
                        break
            sum += ans
        return sum


print(part1('08.in'))
print(part2('08.in'))
