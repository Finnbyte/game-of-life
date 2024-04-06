    def _count_live_neighbors(self, row: int, col: int) -> int:
        alive_neighbors = 0
        for y in range(row - 1, row + 2):
            for x in range(col - 1, col + 2):
                if 0 <= y < GRID_SIZE and 0 <= x < GRID_SIZE and not (y == row and x == col):
                    if self.get(y, x) == 1:
                        alive_neighbors += 1
        print(f"alive_neighbors for y{y} x{x}: {alive_neighbors}")
        return alive_neighbors
