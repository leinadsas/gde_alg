import random
import UI
import Config 

# Feladata: A tábla logikai reprezentációja.
# Tárolja a tiltott mezőket.
# Segédfüggvényeket adhat a mezők érvényességének ellenőrzésére.

def generate_grid(m):
    start = (m - 1, 0)
    end = (0, m - 1)
    cell = 0
    
    
    def is_reserved(cell):
        return cell == start or cell == end or \
               cell in get_neighbors(*start) or cell in get_neighbors(*end)
               
    
    # Szomszédokat meghatározó segédfüggvény
    def get_neighbors(i, j):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < m:
                neighbors.append((ni, nj))
        return neighbors

    # Tiltott zóna: ahol biztosan nem lehet akadály
    reserved = {start, end}
    reserved |= set(get_neighbors(*start))
    reserved |= set(get_neighbors(*end))

    # Próbáljuk újragenerálni, amíg bejárható labirintust nem kapunk
    while True:
        forbidden = set()
        blocked_count = 0
        attempts = 0
        max_attempts = 1000  # nehogy végtelen ciklus legyen

        while blocked_count < m and attempts < max_attempts:
            i = random.randint(0, m - 1)
            j = random.randint(0, m - 1)
            cell = (i, j)
            if is_reserved(cell) or cell in forbidden:
                attempts += 1
                continue
            forbidden.add(cell)
            blocked_count += 1

          # Csak akkor fogadjuk el, ha bejárható a cél és nincs tiltott mező tiltott zónában
        if not forbidden & reserved and Config.is_reachable(m, forbidden):
            return forbidden