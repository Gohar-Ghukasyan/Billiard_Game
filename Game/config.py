import math
import numpy as np
import pygame


def get_default_font(size):
    font_defualt = pygame.font.get_default_font()
    return pygame.font.Font(font_defualt, size)


def white_ball_initial_pos():
    infoObject = pygame.display.Info()
    global resolution
    resolution = np.array([infoObject.current_w, infoObject.current_h])
    return resolution * [0.25, 0.5]


fullscreen = False

if not fullscreen:
    resolution = np.array([1000, 500])

window_caption = "8 Ball Pool Game"

table_margin = 30

table_side_color = (51, 17, 0)

table_color = (0, 100, 0)

separation_line_color = (200, 200, 200)

hole_radius = 20
middle_hole_offset = np.array([[- hole_radius * 2, hole_radius], [-hole_radius, 0],
                               [hole_radius, 0], [hole_radius * 2, hole_radius]])
side_hole_offset = np.array([
    [- 2 * math.cos(math.radians(45)) * hole_radius - hole_radius, hole_radius],
    [- math.cos(math.radians(45)) * hole_radius, - math.cos(math.radians(45)) * hole_radius],
    [math.cos(math.radians(45)) * hole_radius, math.cos(math.radians(45)) * hole_radius],
    [- hole_radius, 2 * math.cos(math.radians(45)) * hole_radius + hole_radius]
])

player1_cue_color = (255, 0, 0)
player2_cue_color = (0, 0, 255)
cue_hit_power = 3
cue_length = 250
cue_thickness = 3
cue_max_displacement = 100

cue_safe_displacement = 1
aiming_line_length = 30
total_ball_num = 16
ball_radius = 14
ball_mass = 14
speed_angle_threshold = 0.09
visible_angle_threshold = 0.05
ball_colors = [
    (255, 255, 255),
    (0, 105, 204),
    (0, 204, 0),
    (179, 45, 0),
    (230, 115, 0),
    (200, 0, 0),
    (153, 0, 153),
    (119, 119, 60),
    (0, 0, 0),
    (102, 0, 102),
    (179, 89, 0),
    (150, 0, 0),
    (102, 26, 0),
    (153, 153, 0),
    (26, 51, 0),
    (0, 40, 77)
]
ball_stripe_thickness = 5
ball_stripe_point_num = 25

ball_starting_place_ratio = [0.75, 0.5]


if 'resolution' in locals():
    white_ball_initial_pos = resolution * [0.25, 0.5]


ball_label_text_size = 11


friction_threshold = 0.06
friction_coeff = 0.99

ball_coeff_of_restitution = 0.9
table_coeff_of_restitution = 0.9
player1_target_text = 'P1 balls  -  '
player2_target_text = 'P2 balls  -  '
target_ball_spacing = 3
game_over_label_font_size = 40
