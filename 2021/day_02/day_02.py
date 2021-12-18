class Day_02:
    def read_input(self, file_name: str):
        with open(file_name) as f:
            self.cmds = [x.strip() for x in f.readlines()]
        return None

    def part1(self) -> int:
        pos_x = 0
        pos_y = 0
        for cmd in self.cmds:
            cmd_name, num = cmd.split()
            num = int(num)
            if cmd_name == 'forward':
                pos_x += num
            elif cmd_name == 'down':
                pos_y += num
            elif cmd_name == 'up':
                pos_y -= num
        return pos_x * pos_y

    def part2(self) -> int:
        pos_x = 0
        pos_y = 0
        iam = 0
        for cmd in self.cmds:
            cmd_name, num = cmd.split()
            num = int(num)
            if cmd_name == 'forward':
                pos_x += num
                pos_y += num * iam
            elif cmd_name == 'down':
                iam += num
            elif cmd_name == 'up':
                iam -= num
        return pos_x * pos_y

solution = Day_02()

solution.read_input('test.txt')
print(solution.part1())
print(solution.part2())

solution.read_input('input.txt')
print(solution.part1())
print(solution.part2())