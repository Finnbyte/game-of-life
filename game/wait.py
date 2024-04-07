import pygame

def wait(delay: int, last: int) -> bool:
    """ Waits non-blockingly using tick timings.
    Returns True when wait is complete, else False."""
    elapsed = pygame.time.get_ticks()
    if abs(elapsed - last) < delay:
        return False
    return True
