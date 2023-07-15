import pygame
import numpy
from math import floor

def draw_quadrants(surface):
    board_size = surface.get_width()
    #draw board quadrants
    quadrant_size = board_size/3
    corner_list = [(1,0), (0,1), (2,1), (1,2)]
    for corners in corner_list:
        a, b = corners
        quadrant_rect = pygame.Rect(quadrant_size*a, quadrant_size*b, quadrant_size, quadrant_size)
        pygame.draw.rect(surface, '#3a523c', quadrant_rect)

def draw_lines(surface):
    board_size = surface.get_width()
    house_size = board_size/9
    for n in range(1,9):
        pygame.draw.line(surface, '#6e8270', (n*house_size, 0), (n*house_size, board_size-2)) # subtracting 2 pixels to prevent leaving the frame
        pygame.draw.line(surface, '#6e8270', (0, n*house_size), (board_size-2, n*house_size)) # subtracting 2 pixels to prevent leaving the frame
    """for n in range(0,9):
        n+=0.5
        pygame.draw.line(surface, 'red', (n*house_size, 0), (n*house_size, board_size-2)) # subtracting 2 pixels to prevent leaving the frame
        pygame.draw.line(surface, 'red', (0, n*house_size), (board_size-2, n*house_size)) # subtracting 2 pixels to prevent leaving the frame
    """ 


def draw_numbers(surface, board_string):
    board_size = surface.get_width()
    house_size = board_size/9

    # the ratio between number and margin will be 8:1
    font_size = house_size*0.6
    font_mono = pygame.font.Font('ai_writer_mono.ttf',int(font_size))
    y = house_size*0.11

    for n in range(9):
        x = house_size*0.32
        for char in board_string[n*9:9*(n+1)]:
            if char != '0':
                text = font_mono.render(char, True, '#528d58')
                surface.blit(text, (x, y))
            x += house_size
        y += house_size

def highlight_hovered(surface, mouse_pos):
    board_size = surface.get_width()
    house_size = board_size/9
    board_offset = surface.get_offset()
    x = floor( (mouse_pos[0] - board_offset[0])*9/board_size )
    y = floor( (mouse_pos[1] - board_offset[1])*9/board_size )
    print(x,y)
    hover_rect = pygame.Rect(x*house_size, y*house_size, house_size+1, house_size+1)
    pygame.draw.rect(surface, '#2a5b2f', hover_rect)
