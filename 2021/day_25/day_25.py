import time

with open('input.txt') as f:
    MAP = list()
    for line in f:
        MAP.append(list(line.strip()))
    R = len(MAP)
    C = len(MAP[0])


def step(MAP):
    moved = False
    MAP2 = [[MAP[r][c] for c in range(C)] for r in range(R)]
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == '>' and MAP[i][(j + 1) % C] == '.':
                MAP2[i][j] = '.'
                MAP2[i][(j + 1) % C] = '>'
                moved = True
    MAP3 = [[MAP2[r][c] for c in range(C)] for r in range(R)]
    for i in range(R):
        for j in range(C):
            if MAP2[i][j] == 'v' and MAP2[(i + 1) % R][j] == '.':
                MAP3[i][j] = '.'
                MAP3[(i + 1) % R][j] = 'v'
    return (moved, MAP3)


start_time = time.time()
count = 0
while True:
    moved, MAP = step(MAP)
    if not moved:
        break
    count += 1
    print(count)
print(count + 1)
print(time.time() - start_time)
