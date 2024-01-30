from colors import BLACK, WHITE

class TopPanel:
    def __init__(self, surface, font):
        self.font = font
        self.surface = surface
        
    def render(self, is_editing_grid):
        self.surface.fill(WHITE)
        self.surface.blit(self.font.render(f"{'Editing' if is_editing_grid else 'Simulating'}", True, BLACK), (0,0))
