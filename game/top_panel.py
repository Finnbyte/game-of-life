from game.constants import BLACK, WHITE
from game.game_state import GameState

class TopPanel:
    def __init__(self, surface, font):
        self.font = font
        self.surface = surface

    def _build_title(self, game_state: GameState):
        return 'Editing' if game_state == GameState.EDITING else 'Simulating'
        
    def draw(self, game_state):
        self.surface.fill(WHITE)

        title = self._build_title(game_state) 

        GAP = 3
        self.surface.blit(self.font.render(title, True, BLACK), (GAP,GAP))
