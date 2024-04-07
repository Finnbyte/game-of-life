from game.cell_grid import CellGrid 
from game.constants import *
import pygame

class GridRenderer:
    @staticmethod
    def draw_grid(surface: pygame.Surface, grid: CellGrid) -> None:
        for y, x in grid:
            GridRenderer.draw_cell(surface, grid, y, x)

    @staticmethod
    def draw_cell(surface: pygame.Surface, grid: CellGrid, y: int, x: int) -> None:
        alive = grid.is_alive(y, x)
        color = BLACK if alive else WHITE

        cell = pygame.Surface([CELL_SIZE, CELL_SIZE])
        cell.fill(color)

        surface.blit(cell, ((x*CELL_SIZE, y*CELL_SIZE)))
    
    @staticmethod
    def prepare_grid(surface: pygame.Surface):
        for x in range(WINDOW_WIDTH // CELL_SIZE):
            for y in range(WINDOW_HEIGHT // CELL_SIZE):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE,
                    CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(surface, WHITE, rect, 1)