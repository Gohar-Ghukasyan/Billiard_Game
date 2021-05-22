import numpy as np
import pygame


class GameEvent:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data


def events():
    closed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True

    return {"closed": closed,
            "clicked": pygame.mouse.get_pressed()[0],
            "mouse_pos": np.array(pygame.mouse.get_pos())}
