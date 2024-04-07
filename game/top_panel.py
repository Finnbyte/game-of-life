from constants import *
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
        self._slider = Slider(
            WINDOW_WIDTH - SLIDER_WIDTH - (EDGE_GAP * 2),
            EDGE_GAP,
            SLIDER_WIDTH,
            SLIDER_HEIGHT,
            GRAY,
            DARK_GRAY,
            500,
            50,
            70,
        )

    def get_slider_value(self) -> int:
        """Returns slider bar's value."""
        return self._slider.value

    def _build_title(self, game_state: GameState) -> str:
        """Builds top panel title using game's current state."""
        return "Editing" if game_state == GameState.EDITING else "Simulating"

    def handle_slider_event(self, x_axis_value: int):
        """Handles slider bar's event."""
        self._slider.handle_event(self.surface, x_axis_value)

    def mouse_on_slider(self, x: int, y: int) -> bool:
        """Returns True if mouse is clicked on slider."""
        return self._slider.on_slider(x, y)

    def draw(self, game_state: GameState) -> None:
        """Draws top panel."""
        self.surface.fill(WHITE)  # otherwise leaves a buffer of colors and slider balls

        self._slider.draw(self.surface)

        title = self._build_title(game_state)
        self.surface.blit(
            self._font.render(title, True, DARK_GRAY), (EDGE_GAP, EDGE_GAP)
        )
