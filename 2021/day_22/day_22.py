from typing import List


# класс для парсинга входных данных
# пример: on x=-20..26,y=-36..17,z=-47..7
class Cmd:
    def __init__(self, line):
        self.cmd, coords = line.strip().split()
        x, y, z = coords.split(',')
        self.start_x = int(x[2:].split('.')[0])
        self.end_x = int(x[2:].split('.')[2])
        self.start_y = int(y[2:].split('.')[0])
        self.end_y = int(y[2:].split('.')[2])
        self.start_z = int(z[2:].split('.')[0])
        self.end_z = int(z[2:].split('.')[2])


class Day_22:
    def part1(self, file_name: str) -> int:
        # просто моделируем весь процесс
        # под все возможные кубы заводим переменную с координатами, трехмерный массив
        # начальное значение для всех кубов False
        cubes = list()
        for x in range(-50, 50 + 1):
            new_x = list()
            for y in range(-50, 50 + 1):
                new_y = list()
                for z in range(-50, 50 + 1):
                    new_y.append(False)
                new_x.append(new_y)
            cubes.append(new_x)

        with open(file_name) as f:
            for line in f:
                # парсим входные данные по каждой строке
                new_cmd = Cmd(line)
                # накладываем ограничения -50..50
                start_x = max(-50, new_cmd.start_x)
                end_x = min(50, new_cmd.end_x)
                start_y = max(-50, new_cmd.start_y)
                end_y = min(50, new_cmd.end_y)
                start_z = max(-50, new_cmd.start_z)
                end_z = min(50, new_cmd.end_z)
                # само моделирование, помечаем кубы текущей командой on/off
                for x in range(start_x, end_x + 1):
                    for y in range(start_y, end_y + 1):
                        for z in range(start_z, end_z + 1):
                            cubes[x][y][z] = (new_cmd.cmd == 'on')
        # считаем кол-во кубов on/off
        count_on = 0
        for x in range(-50, 50 + 1):
            for y in range(-50, 50 + 1):
                for z in range(-50, 50 + 1):
                    if cubes[x][y][z]:
                        count_on += 1
        return count_on

    def part2(self, file_name: str) -> int:
        # строим сетку по всевозможным координатам
        # т.е. мы будем оперировать не каждым кубом, а секторами
        # границами каждого сектора могут быть только границы из поступивших команд
        x_line = list()
        y_line = list()
        z_line = list()
        # списоок команд
        cmds = list()
        with open(file_name) as f:
            for line in f:
                # парсим каждую сроку входного файла
                new_cmd = Cmd(line)
                # увеличиваем конец интервала, например интервал (1, 1) начинается в точке 1 и заканчивается в точке 2
                new_cmd.end_x += 1
                new_cmd.end_y += 1
                new_cmd.end_z += 1
                cmds.append(new_cmd)
                # запоминаем возможные координаты границ секторов которые будем проверять
                x_line.append(new_cmd.start_x)
                x_line.append(new_cmd.end_x)
                y_line.append(new_cmd.start_y)
                y_line.append(new_cmd.end_y)
                z_line.append(new_cmd.start_z)
                z_line.append(new_cmd.end_z)
        # сортируем координаты и перебираем все возможные сектора
        # для каждого сектора будем прогонять все команды и смотреть включен сектор или нет
        x_line.sort()
        y_line.sort()
        z_line.sort()
        count_on = 0
        for i in range(len(x_line) - 1):
            # вывод на экран прогресса
            print(int(i/len(x_line) * 1000)/10)
            # оптимизация для ускорения
            # выбираем только те команды которые воздействуют на секторы с текущим интервалом по оси х
            # если команда не воздействует на текущий интервал по оси х смотреть другие оси нет смысла
            can_cmd_x = set()
            for cmd_i in range(len(cmds)):
                if x_line[i] >= cmds[cmd_i].start_x and x_line[i + 1] <= cmds[cmd_i].end_x:
                    can_cmd_x.add(cmd_i)
            if not can_cmd_x:
                continue
            # конец оптимизации
            for j in range(len(y_line) - 1):
                # ищем только те команды которые воздействую на сектора с текущим y
                can_cmd_xy = set()
                for cmd_i in can_cmd_x:
                    if y_line[j] >= cmds[cmd_i].start_y and y_line[j + 1] <= cmds[cmd_i].end_y:
                        can_cmd_xy.add(cmd_i)
                if not can_cmd_xy:
                    continue
                # конец оптимизации для оси y
                for k in range(len(z_line) - 1):
                    last_cmd = 'off'
                    for cmd_i in sorted(can_cmd_xy, reverse=True):
                        if z_line[k] >= cmds[cmd_i].start_z and z_line[k + 1] <= cmds[cmd_i].end_z:
                            last_cmd = cmds[cmd_i].cmd
                            break
                    if last_cmd == 'on':
                        count = (x_line[i + 1] - x_line[i]) * (y_line[j + 1] - y_line[j]) * (z_line[k + 1] - z_line[k])
                        count_on += count
        return count_on


solution = Day_22()

ans_test_1 = solution.part1('test_1.txt')
print(ans_test_1)
assert ans_test_1 == 590784

ans_part_1 = solution.part1('input.txt')
print(ans_part_1)
assert ans_part_1 == 610196

ans_test_2 = solution.part2('test_2.txt')
print(ans_test_2)
assert ans_test_2 == 2758514936282235

ans_part_2 = solution.part2('input.txt')
print(ans_part_2)
assert ans_part_2 == 1282401587270826
