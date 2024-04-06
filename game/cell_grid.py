import numpy as np
from math import ceil
from typing import Self
from game.ruleset import is_allowed_to_live
from game.constants import GRID_SIZE
import pygame
from copy import deepcopy

class CellGrid:
    def __init__(self, template: list[list[int]] | None = None):
        if template is not None:
            self._grid = template
        else:
            self._grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    
    def get(self, y: int, x: int) -> int:
        return self._grid[y][x]

    def set(self, y: int, x: int, state: int) -> None:
        self._grid[y][x] = state

    def _count_live_neighbors(self, row: int, col: int) -> int:
        alive_neighbors = 0
        for y in range(row - 1, row + 2):
            for x in range(col - 1, col + 2):
                if 0 <= y < GRID_SIZE and 0 <= x < GRID_SIZE and not (y == row and x == col):
                    if self.get(y, x) == 1:
                        alive_neighbors += 1
        return alive_neighbors
 
    @staticmethod
    def process_next(curr: Self) -> Self:
        next_generation_grid = np.zeros_like(curr._grid)
        for y, x in curr:
            alive_neighbors = curr._count_live_neighbors(y, x)
            if is_allowed_to_live(curr.get(y, x) == 1, alive_neighbors):
                next_generation_grid[y][x] = 1

        return CellGrid(template=next_generation_grid)

    def __iter__(self):
        for y, x in np.ndindex(self._grid.shape):
            yield y, x
