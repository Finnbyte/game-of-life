from game.constants import *
import pygame
from game.game_state import GameState
from game.slider import Slider

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
    def handle_slider_event(self, x_axis_value: int):
        self._slider.handle_event(self.surface, x_axis_value)


    def mouse_on_slider(self, x: int, y: int) -> bool:
        return self._slider.on_slider(x, y)
        
    def draw(self, game_state):
        self.surface.fill(WHITE)

        title = self._build_title(game_state) 

        GAP = 3
        self.surface.blit(self.font.render(title, True, BLACK), (GAP,GAP))
