from lib.cell_helpers import count_live_neighbors, should_die
import numpy as np
from math import ceil
import pygame
from copy import deepcopy
from colors import DARK_GRAY, WHITE

class CellGrid:
    def __init__(self, surface, grid_size: int, y_offset: int):
        self.is_editing_grid = True        
        self._Y_OFFSET = y_offset
        self.surface = surface
        self._GRID_SIZE = grid_size
        self._CELL_SIZE = 20

    def initialize_cells(self):
        self.cells = np.zeros((self._GRID_SIZE, self._GRID_SIZE), dtype=int)

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

        self.blit_cell_at(row, col, DARK_GRAY if new_aliveness == 1 else WHITE)

    def update(self):
        next_generation_cells = np.zeros((self.cells.shape[0], self.cells.shape[1]), dtype=int)

        for y, x in np.ndindex(self.cells.shape):
            alive_neighbors = count_live_neighbors(self.cells, self._GRID_SIZE, y, x)
            color = WHITE

            if not should_die(self.cells[y][x] == 1, alive_neighbors):
                color = DARK_GRAY
                next_generation_cells[y][x] = 1

            self.blit_cell_at(y, x, color)

        self.cells = next_generation_cells

    def draw(self, surface):
        for y in range(0, self._GRID_SIZE):
            for x in range(0, self._GRID_SIZE):
                pygame.draw.rect(surface, DARK_GRAY if self.cells[y][x] == 1 else WHITE, 
                    (x*self._CELL_SIZE, y*self._CELL_SIZE, self._CELL_SIZE-1, self._CELL_SIZE-1))

    def blit_cell_at(self, y, x, color):
        cell = pygame.Surface([self._CELL_SIZE-1, self._CELL_SIZE-1])
        cell.fill(color)
        self.surface.blit(cell, ((x*self._CELL_SIZE, y*self._CELL_SIZE)))