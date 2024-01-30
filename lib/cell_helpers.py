neighbor_offsets = (
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

def count_live_neighbors(cells: list[list[int]], cells_size: int, row_index: int, column_index: int) -> bool:
    alive_neighbors = 0
    for y, x in neighbor_offsets:
        potential_cell_y = row_index + y
        potential_cell_x = column_index + x

        if 0 <= potential_cell_y < cells_size and 0 <= potential_cell_x < cells_size:
            if cells[potential_cell_y][potential_cell_x] == 1:
                alive_neighbors += 1

    return alive_neighbors

def should_die(is_alive: int, alive_neighbors: int):
    if (is_alive and (alive_neighbors == 3 or alive_neighbors == 2)) or not is_alive and alive_neighbors == 3:
        return False
    return True