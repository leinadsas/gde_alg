import random
import UI
from UI import m  # UI modulból importáljuk az 'm' értéket

# Feladata: A tábla logikai reprezentációja.
# Tárolja a tiltott mezőket.
# Segédfüggvényeket adhat a mezők érvényességének ellenőrzésére.

def generate_grid(m):
    # Üres m x m mátrix, minden mező kezdetben 1
    grid = [[1 for _ in range(m)] for _ in range(m)]

    # Tiltott mezők száma legfeljebb m
    blocked_count = 0
    max_blocked = m
    forbidden = set()

    # Segédfüggvény: adott pozíció körüli koordináták
    def get_neighbors(i, j):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < m:
                neighbors.append((ni, nj))
        return neighbors

    # Tiltott mezők elhelyezése
    while blocked_count < max_blocked:
        i = random.randint(0, m - 1)
        j = random.randint(0, m - 1)

        # Ne legyen tiltott mező a start vagy cél mező körül
        if (i, j) == (m - 1, 0) or (i, j) == (0, m - 1):
            continue
        if (i, j) in get_neighbors(m - 1, 0) or (i, j) in get_neighbors(0, m - 1):
            continue
        if (i, j) in forbidden:
            continue  # már tiltott

        grid[i][j] = 0
        forbidden.add((i, j))
        blocked_count += 1

    return forbidden