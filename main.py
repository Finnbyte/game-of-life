import pygame
from math import ceil
from copy import deepcopy

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
DARK_GRAY = (105,105,105)

WINDOW_WIDTH = 550
WINDOW_HEIGHT = 550
GRID_SIZE = 500
CELL_SIZE = 20

TOP_OFFSET = (CELL_SIZE * 2) - 1

grid = [[0] * GRID_SIZE for i in range(WINDOW_HEIGHT)]

def main():
    pygame.init()

    pygame.display.set_caption("Game of Life :D")
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    top_panel_surface = pygame.Surface((WINDOW_WIDTH, TOP_OFFSET))

    grid_surface = pygame.Surface((GRID_SIZE, GRID_SIZE))
    draw_grid(grid_surface)
    grid_surface.fill(GRAY)

    running = True
    is_editing_grid = True
    while running:
        top_panel_surface.fill(WHITE)

        top_panel_surface.blit(font.render(f"{'Editing' if is_editing_grid else 'Simulating'}", True, BLACK), (0,0))
        SCREEN.blit(top_panel_surface, (0, 0))

        draw_grid_cells(grid_surface)
        SCREEN.blit(grid_surface, (0, TOP_OFFSET))

        if not is_editing_grid:
            process_generation(grid)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_editing_grid = not is_editing_grid
            if event.type == pygame.MOUSEBUTTONUP:
                if is_editing_grid:
                    handle_cell_click_during_setup(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        pygame.display.update()
        CLOCK.tick(30)
        
    sys.exit()

def get_grid_indices_from_mouse_pos(pos) -> tuple[int, int]:
    x, y = pos
    # offset by -1 to make into 0-based indexing
    row = ceil((y - TOP_OFFSET) / CELL_SIZE) - 1
    col = ceil(x / CELL_SIZE) - 1
    return (row, col)

def handle_cell_click_during_setup(pos):
    row, col = get_grid_indices_from_mouse_pos(pos)
    new_aliveness = grid[row][col] ^ 1
    grid[row][col] = new_aliveness

def count_live_neighbors(cells: list[list[int]], row_index: int, column_index: int) -> bool:
    neighbors = (
        # top
        (-1, -1),
        (-1, 0),
        (-1, 1),
        # center
        (0, -1),
        (0, 1),
        # bottom
        (1, -1),
        (1, 0),
        (1, 1)
    )

    alive_neighbors = 0
    for y, x in neighbors:
        potential_cell_y = row_index + y
        potential_cell_x = column_index + x

        if 0 <= potential_cell_y < GRID_SIZE and 0 <= potential_cell_x < GRID_SIZE:
            if cells[potential_cell_y][potential_cell_x] == 1:
                alive_neighbors += 1

    return alive_neighbors

def should_die(is_alive: int, alive_neighbors: int):
    if (is_alive and (alive_neighbors == 3 or alive_neighbors == 2)) or not is_alive and alive_neighbors == 3:
        return False
    return True
 
def process_generation(cells: list[list[int]]):
    next_generation_cells = deepcopy(cells)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            alive_neighbors = count_live_neighbors(cells, i, j)
            if should_die(cells[i][j] == 1, alive_neighbors):
                next_generation_cells[i][j] = 0
            else:
                next_generation_cells[i][j] = 1

    for y, row in enumerate(next_generation_cells):
        for x, aliveness in enumerate(row):
            cells[y][x] = aliveness

def draw_grid(surface):
    for y in range(0, GRID_SIZE):
        for x in range(0, GRID_SIZE):
            outline = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GRAY, outline, 3)
            

def draw_grid_cells(surface):
    for y in range(0, GRID_SIZE):
        for x in range(0, GRID_SIZE):
            cell = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 3, CELL_SIZE - 3)
            pygame.draw.rect(surface, DARK_GRAY if grid[y][x] == 1 else WHITE, cell, CELL_SIZE)

    
if __name__ == "__main__":
    main()