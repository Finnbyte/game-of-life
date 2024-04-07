from game.constants import BLACK, WHITE
from game.game_state import GameState
EDGE_GAP = 10
SLIDER_WIDTH = 150
SLIDER_HEIGHT = 20

class TopPanel:
    def __init__(self, surface, font) -> None:
        self.surface = surface
        self._font = font
        self._slider = Slider(WINDOW_WIDTH - SLIDER_WIDTH - (EDGE_GAP * 2), EDGE_GAP, 
           SLIDER_WIDTH, SLIDER_HEIGHT,
           GRAY, DARK_GRAY, 50, 500, 70)
    

    def get_slider_value(self) -> int:
        return self._slider.value

    def _build_title(self, game_state: GameState):
        return 'Editing' if game_state == GameState.EDITING else 'Simulating'
        
    def draw(self, game_state):
        self.surface.fill(WHITE)

        title = self._build_title(game_state) 

        GAP = 3
        self.surface.blit(self.font.render(title, True, BLACK), (GAP,GAP))
