import Solver
import Grid
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def plot_grid(m, forbidden, start=(0, 0), end=None):
    """
    :param m: A rács mérete (m x m) - külső változóból jön
    :param forbidden: Tiltott mezők halmaza (pl. {(1, 1), (2, 2)}) - külső változóból jön
    :param start: Kezdőpont (alapértelmezett: (0, 0))
    :param end: Célpont (alapértelmezett: (m-1, m-1))
    """
    if end is None:
        end = (m-1, m-1)

    # Rács inicializálása
    grid = np.zeros((m, m))
    grid[start[0], start[1]] = 1  # Kezdőpont
    grid[end[0], end[1]] = 2      # Célpont
    for (i, j) in forbidden:
        grid[i, j] = 3            # Tiltott mezők

    # Színtérkép
    cmap = ListedColormap(['white', 'green', 'red', 'black'])

    # Ablak létrehozása
    fig, ax = plt.subplots(figsize=(8, 8))
    img = ax.imshow(grid, cmap=cmap, extent=[0, m, 0, m], origin='lower')

    # Rácsvonalak
    ax.set_xticks(np.arange(0, m, 1))
    ax.set_yticks(np.arange(0, m, 1))
    ax.grid(which='both', color='gray', linestyle='-', linewidth=0.5)

    # Címkék
    forbidden = Grid.generate_grid(m)
    dp, result2 = Solver.count_paths(m, forbidden)
    ax.set_title(f"Rács: {m}x{m} | Tiltott mezők: {len(forbidden)} | Utak száma:{result2}", pad=20)
    plt.colorbar(img, ticks=[0.5, 1.0, 2.0, 2.5]).ax.set_yticklabels(['Szabad', 'Kezdő', 'Cél', 'Tiltott'])

    plt.show()

#plot_grid(m, forbidden)