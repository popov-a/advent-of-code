class Day_05:
    def part1(self, file_name: str) -> int:
        matrix = [[0] * 1000 for i in range(1000)]
        max_count = 0
        with open(file_name) as f:
            for line in f:
                start, end = line.strip().split(' -> ')
                x1, y1 = map(int, start.split(','))
                x2, y2 = map(int, end.split(','))
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        matrix[y][x1] += 1
                        if matrix[y][x1] == 2:
                            max_count += 1
                elif y1 == y2:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        matrix[y1][x] += 1
                        if matrix[y1][x] == 2:
                            max_count += 1
        return max_count

    def part2(self, file_name: str) -> int:
        matrix = [[0] * 1000 for i in range(1000)]
        max_count = 0
        with open(file_name) as f:
            for line in f:
                start, end = line.strip().split(' -> ')
                x1, y1 = map(int, start.split(','))
                x2, y2 = map(int, end.split(','))
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        matrix[y][x1] += 1
                        if matrix[y][x1] == 2:
                            max_count += 1
                elif y1 == y2:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        matrix[y1][x] += 1
                        if matrix[y1][x] == 2:
                            max_count += 1
                elif (y2 - y1) == (x2 - x1):
                    for di in range(abs(y2 - y1) + 1):
                        matrix[min(y1, y2) + di][min(x1, x2) + di] += 1
                        if matrix[min(y1, y2) + di][min(x1, x2) + di] == 2:
                            max_count += 1
                elif (y2 - y1) == (x1 - x2):
                    for di in range(abs(y2 - y1) + 1):
                        matrix[max(y1, y2) - di][min(x1, x2) + di] += 1
                        if matrix[max(y1, y2) - di][min(x1, x2) + di] == 2:
                            max_count += 1
        return max_count


solution = Day_05()
print(solution.part1('test.txt'))
print(solution.part2('test.txt'))
print(solution.part1('input.txt'))
print(solution.part2('input.txt'))
