from colors import BLACK, WHITE

class TopPanel:
    def __init__(self, font):
        self.font = font
        
    def draw(self, surface, is_editing_grid):
        surface.fill(WHITE)
        surface.blit(self.font.render(f"{'Editing' if is_editing_grid else 'Simulating'}", True, BLACK), (0,0))
