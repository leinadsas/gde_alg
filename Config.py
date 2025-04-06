import os
from collections import deque
# Feladata: kisebb függvények tárolása

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_reachable(m, forbidden):
    start = (m - 1, 0)
    goal = (0, m - 1)
    visited = set()
    queue = deque([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        i, j = queue.popleft()
        if (i, j) == goal:
            return True
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < m and (ni, nj) not in forbidden and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj))
    return False