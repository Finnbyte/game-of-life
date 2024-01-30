import pygame
from math import ceil
from copy import deepcopy
from cell_grid import CellGrid
from top_panel import TopPanel

WINDOW_WIDTH = 550
WINDOW_HEIGHT = 550
GRID_SIZE = 550
CELL_SIZE = 20

TOP_OFFSET = (CELL_SIZE * 2) - 1
GRID_X_PADDING = 10

def main():
    pygame.init()
    pygame.display.set_caption("Game of Life :D")

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.SysFont(None, 32)

    cell_grid = CellGrid(GRID_SIZE, TOP_OFFSET)
    cell_grid.initialize_cells()

    top_panel_surface = pygame.Surface((WINDOW_WIDTH, TOP_OFFSET))
    top_panel = TopPanel(font)

    grid_surface = pygame.Surface((GRID_SIZE, GRID_SIZE))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                cell_grid.is_editing_grid = not cell_grid.is_editing_grid
            if event.type == pygame.MOUSEBUTTONUP:
                cell_grid.handle_click_on_cell(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        SCREEN.blit(top_panel_surface, (0, 0))
        top_panel.draw(top_panel_surface, cell_grid.is_editing_grid)

        SCREEN.blit(grid_surface, (0, TOP_OFFSET))
        cell_grid.draw(grid_surface)

        if not cell_grid.is_editing_grid:
            cell_grid.update()

        pygame.display.update()
        
    sys.exit()

if __name__ == "__main__":
    import cProfile as profile
    main()