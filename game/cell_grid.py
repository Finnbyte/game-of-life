import numpy as np
from math import ceil
from game.constants import GRID_SIZE
import pygame

ALIVE = 1
DEAD = 0

def is_allowed_to_live(currently_alive: bool, alive_neighbors: int) -> bool:
    can_stay_alive = currently_alive and (alive_neighbors == 3 or alive_neighbors == 2)
    can_resurrect = not currently_alive and alive_neighbors == 3

    return True if can_stay_alive or can_resurrect else False

class CellGrid:
    def __init__(self, template: list[list[int]] | None = None):
        if template is not None:
            self._grid = template
        else:
            self._grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    
    
    def is_alive(self, y: int, x: int) -> bool:
        """Returns True if cell in y,x is alive."""
        return self._grid[y][x] == ALIVE


    def set_alive(self, y: int, x: int) -> None:
        """Sets cell at y,x to be alive."""
        self._grid[y][x] = ALIVE


    def set_dead(self, y: int, x: int) -> None:
        """Sets cell at y,x to be dead."""
        self._grid[y][x] = DEAD


    def _count_alive_neighbors(self, row: int, col: int) -> int:
        """Counts alive neighbors of row, col."""
        alive_neighbors = 0
        for y in range(row - 1, row + 2):
            for x in range(col - 1, col + 2):
                if 0 <= y < GRID_SIZE and 0 <= x < GRID_SIZE and not (y == row and x == col):
                    if self.is_alive(y, x):
                        alive_neighbors += 1
        return alive_neighbors

 
    def process_next(self) -> None:
        """Processes next generation of this grid."""
        next_generation_grid = np.zeros_like(self._grid)
        for y, x in self:
            alive_neighbors = self._count_alive_neighbors(y, x)
            is_alive = self.is_alive(y, x)
            if is_allowed_to_live(is_alive, alive_neighbors):
                next_generation_grid[y][x] = ALIVE

        self._grid = next_generation_grid


    def __iter__(self):
        for y, x in np.ndindex(self._grid.shape):
            yield y, x
