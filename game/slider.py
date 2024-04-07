import pygame


class Slider:
    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        bg_color: tuple[int],
        ball_color: tuple[int],
        min_value: int,
        max_value: int,
        initial_value: int | None = None,
    ) -> None:
        self.sliderRect = pygame.Rect(x, y, w, h)
        self.ball_color = ball_color
        self.bg_color = bg_color
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value or min_value

    def draw(self, screen):
        """Draws slider bar."""
        pygame.draw.rect(screen, self.bg_color, self.sliderRect)
        # Calculate the position of the circle based on the current value
        circle_x = int(
            self.sliderRect.x
            + (self.value - self.min_value)
            / (self.max_value - self.min_value)
            * self.sliderRect.w
        )
        pygame.draw.circle(
            screen,
            self.ball_color,
            (circle_x, self.sliderRect.centery),
            int(self.sliderRect.h * 0.75),
        )

    def get_value(self):
        """Returns instance's current value."""
        return self.value

    def update_value(self, x):
        """Updates slider bar's value."""
        # Calculate the new value based on the position of the slider
        percent = (x - self.sliderRect.x) / self.sliderRect.w
        self.value = self.min_value + percent * (self.max_value - self.min_value)

    def on_slider(self, x, y):
        """Checks if slider bar's rectangle collides with xy."""
        return self.sliderRect.collidepoint(x, y)

    def handle_event(self, screen, x):
        """Handles event."""
        # Ensure the slider stays within its bounds
        x = max(self.sliderRect.x, min(self.sliderRect.x + self.sliderRect.w, x))
        self.update_value(x)
        self.draw(screen)
        print(self.value)
