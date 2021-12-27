from typing import List
from collections import deque, defaultdict, Counter



def solve():
    A1 = 1
    A2 = 2
    B1 = 3
    B2 = 4
    C1 = 5
    C2 = 6
    D1 = 7
    D2 = 8

    def points_to_move(crab, i):

        pass

    steps = [0] * 8
    position = [10, 11, 12, 13, 14, 15, 16, 17]
    crabs = [B1, A1, C1, D1, B2, C2, D2, A2]
    points = 0
    min_points = 1000000

    def win():
        for i in range(8):
            if (crabs[i] == A1 or crabs[i] == A2) and position[i] not in (10, 11):
                return False
            if (crabs[i] == B1 or crabs[i] == B2) and position[i] not in (12, 13):
                return False
            if (crabs[i] == C1 or crabs[i] == C2) and position[i] not in (14, 15):
                return False
            if (crabs[i] == D1 or crabs[i] == D2) and position[i] not in (16, 17):
                return False
        return True

    def rec():
        nonlocal points
        nonlocal min_points

        if win():
            if points < min_points:
                min_points = points
            return

        for crab in range(8):
            if steps[crab] < 5:
                for i in range(1, 17 + 1):
                    if points_to_move(crab, i) < 1000000:
                        p = position[crab]
                        points_ = points
                        points += points_to_move(crab, i)
                        position[crab] == i
                        rec()
                        points = points_
                        position[crab] = p
        return None

    rec()
    return points
