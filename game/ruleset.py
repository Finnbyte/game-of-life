def is_allowed_to_live(currently_alive: bool, alive_neighbors: int) -> bool:
    can_stay_alive = currently_alive and (alive_neighbors == 3 or alive_neighbors == 2)
    can_resurrect = not currently_alive and alive_neighbors == 3

    return True if can_stay_alive or can_resurrect else False
