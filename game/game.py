from sys import exit
import pygame
from game.constants import *
from math import ceil
from game.wait import wait
from game.game_state import GameState
from game.cell_grid import CellGrid
from game.top_panel import TopPanel
from enum import Enum
from game.grid_renderer import GridRenderer

def convert_pygame_xy_to_rowcols(pos):
    x, y = pos
    # offset by -1 to make into 0-based indexing
    row = ceil((y - TOP_PANEL_HEIGHT) / CELL_SIZE) - 1
    col = ceil(x / CELL_SIZE) - 1
    return (row, col)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game of Life")

        self.state = GameState.EDITING
        self.grid = CellGrid()

        self.last = 0

        self.SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.grid_surface = pygame.Surface((GRID_SIZE*CELL_SIZE, GRID_SIZE*CELL_SIZE))
        self.grid_surface.fill(WHITE)

        font = pygame.font.SysFont(None, 32)
        self.top_panel = TopPanel(pygame.Surface((WINDOW_WIDTH, TOP_PANEL_HEIGHT)), font)

    def run_until_quit(self):
        self.top_panel.draw(self.state)
        GridRenderer.prepare_grid(self.grid_surface)
        while True:
            self._handle_events(pygame.event.get())
            self._update()

    def _handle_events(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = GameState.EDITING if self.state == GameState.SIMULATING else GameState.SIMULATING
                self.top_panel.draw(self.state)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.top_panel.mouse_on_slider(*event.pos):
                    self.top_panel.handle_slider_event(event.pos[0])
                    self.top_panel.draw(self.state)
            if event.type == pygame.MOUSEBUTTONUP:
                if self.state != GameState.EDITING:
                    return

                row, col = convert_pygame_xy_to_rowcols(pygame.mouse.get_pos())
                new_aliveness = self.grid.get(row, col)^1

                self.grid.set(row, col, new_aliveness)
                GridRenderer.draw_cell(self.grid_surface, self.grid, 
                    row, col)

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                self._handle_quit()
    
    def _update(self):
        self.SCREEN.blit(self.top_panel.surface, (0, 0))
        self.SCREEN.blit(self.grid_surface, (0, TOP_PANEL_HEIGHT))

        ticks_delay = int(self.top_panel.get_slider_value())

        if self.state == GameState.SIMULATING and wait(ticks_delay, self.last):
            self.last = pygame.time.get_ticks()
            self.grid = CellGrid.process_next(self.grid)
            GridRenderer.draw_grid(self.grid_surface, self.grid)
 
        pygame.display.update()

    def _handle_quit(self):
        pygame.quit()
        exit()

    def draw_cell(self, y, x, color):
        cell = pygame.Surface([CELL_SIZE, CELL_SIZE])
        cell.fill(color)
        
        self.grid_surface.blit(cell, ((x*CELL_SIZE, y*CELL_SIZE)))
