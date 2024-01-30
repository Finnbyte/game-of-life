from lib.cell_helpers import count_live_neighbors, should_die
from math import ceil
import pygame
from copy import deepcopy
from colors import DARK_GRAY, WHITE

class CellGrid:
    def __init__(self, grid_size: int, y_offset: int):
        self.is_editing_grid = True        
        self._Y_OFFSET = y_offset
        self._GRID_SIZE = grid_size
        self._CELL_SIZE = 20

    def initialize_cells(self):
        self.cells = [[0] * self._GRID_SIZE for i in range(self._GRID_SIZE)]

    def _convert_pygame_xy_to_rowcols(self, pos):
        x, y = pos
        # offset by -1 to make into 0-based indexing
        row = ceil((y - self._Y_OFFSET) / self._CELL_SIZE) - 1
        col = ceil(x / self._CELL_SIZE) - 1
        return (row, col)

    def handle_click_on_cell(self, pos):
        if not self.is_editing_grid:
            return
        row, col = self._convert_pygame_xy_to_rowcols(pos)
        new_aliveness = self.cells[row][col]^1
        self.cells[row][col] = new_aliveness

    def update(self):
        next_generation_cells = deepcopy(self.cells)

        for i in range(self._GRID_SIZE):
            for j in range(self._GRID_SIZE):
                alive_neighbors = count_live_neighbors(self.cells, self._GRID_SIZE, i, j)
                if should_die(self.cells[i][j] == 1, alive_neighbors):
                    next_generation_cells[i][j] = 0
                else:
                    next_generation_cells[i][j] = 1

        for y, row in enumerate(next_generation_cells):
            for x, aliveness in enumerate(row):
                self.cells[y][x] = aliveness

    def draw(self, surface):
        for y in range(0, self._GRID_SIZE):
            for x in range(0, self._GRID_SIZE):
                pygame.draw.rect(surface, DARK_GRAY if self.cells[y][x] == 1 else WHITE, 
                    (x*self._CELL_SIZE, y*self._CELL_SIZE, self._CELL_SIZE-1, self._CELL_SIZE-1))