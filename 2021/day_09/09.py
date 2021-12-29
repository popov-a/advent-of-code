from typing import List
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def is_low(r, c: int, m: List[List[int]]) -> bool:
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < R and 0 <= cc < C and m[r][c] >= m[rr][cc]:
            return False
    return True


def get_basin_size(r, c: int, m: List[List[int]]) -> int:
    lst = list()
    lst.append((r, c))
    st = set()
    st.add((r, c))
    i = 0
    while i < len(lst):
        r, c = lst[i]
        for j in range(4):
            rr = r + dr[j]
            cc = c + dc[j]
            if 0 <= rr < R and 0 <= cc < C and (rr, cc) not in st and m[rr][cc] != 9:
                lst.append((rr, cc))
                st.add((rr, cc))
        i += 1
    return len(st)


m = list()
with open('09.in') as f:
    for line in f:
        line = line.strip()
        m.append([int(x) for x in line])
    R = len(m)
    C = len(m[0])

sum_ = 0
basins = list()
for r in range(len(m)):
    for c in range(len(m[0])):
        if is_low(r, c, m):
            sum_ += 1 + m[r][c]
            basins.append((r, c))

print(sum_)
basin_sizes = list()
for basin in basins:
    basin_sizes.append(get_basin_size(basin[0], basin[1], m))
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
