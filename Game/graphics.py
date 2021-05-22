import pygame
import config


class Canvas:
    def __init__(self):
        if config.fullscreen:
            config.white_ball_initial_pos()
            self.surface = pygame.display.set_mode(config.resolution, pygame.FULLSCREEN)
        else:
            self.surface = pygame.display.set_mode(config.resolution)
        self.background = pygame.Surface(self.surface.get_size())
        self.background = self.background.convert()
        self.background.fill(config.table_color)
        self.surface.blit(self.background, (0, 0))


def add_separation_line(canvas):
    pygame.draw.line(canvas.background, config.separation_line_color, (config.white_ball_initial_pos[0], 0),
                     (config.white_ball_initial_pos[0], config.resolution[1]))
