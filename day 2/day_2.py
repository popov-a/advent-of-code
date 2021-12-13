from typing import List

def read_data(file_name: str) -> List[str]:
    cmds = list()
    with open(file_name) as f:
        for line in f:
            cmds.append(line.strip())
    return cmds

def day2_part1(cmds: List[str]) -> int:
    pos_x = 0
    pos_y = 0
    for cmd in cmds:
        cmd_name, num = cmd.split()
        num = int(num)
        if cmd_name == 'forward':
            pos_x += num
        elif cmd_name == 'down':
            pos_y += num
        elif cmd_name == 'up':
            pos_y -= num
    return pos_x * pos_y

def day2_part2(cmds: List[str]) -> int:
    pos_x = 0
    pos_y = 0
    iam = 0
    for cmd in cmds:
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

cmds = read_data('input.txt')
print(day2_part1(cmds))
print(day2_part2(cmds))