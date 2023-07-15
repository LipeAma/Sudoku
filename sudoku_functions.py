import pygame
import numpy

def draw_board(surface):
    board_size = surface.get_width()

    #draw houses
    house_size = board_size/9
    for n in [1,2,4,5,7,8]:
        pygame.draw.line(surface, '#949494', (n*house_size, 0), (n*house_size, board_size-2)) # subtracting 2 pixels to prevent leaving the frame
        pygame.draw.line(surface, '#949494', (0, n*house_size), (board_size-2, n*house_size)) # subtracting 2 pixels to prevent leaving the frame
    """for n in range(0,9):
        n+=0.5
        pygame.draw.line(surface, 'red', (n*house_size, 0), (n*house_size, board_size-2)) # subtracting 2 pixels to prevent leaving the frame
        pygame.draw.line(surface, 'red', (0, n*house_size), (board_size-2, n*house_size)) # subtracting 2 pixels to prevent leaving the frame
"""
    #draw quadrant
    quadrant_size = board_size/3
    for n in [1,2]:
        pygame.draw.line(surface, '#c7c7c7', (n*quadrant_size, 0), (n*quadrant_size, board_size-2), 3) # subtracting 2 pixels to prevent leaving the frame
        pygame.draw.line(surface, '#c7c7c7', (0, n*quadrant_size), (board_size-2, n*quadrant_size), 3) # subtracting 2 pixels to prevent leaving the frame


def draw_numbers(surface, matrix):
    board_size = surface.get_width()
    house_size = board_size/9

    # the ratio between number and margin will be 8:1
    font_size = house_size*0.6
    font_mono = pygame.font.Font('ai_writer_mono.ttf',int(font_size))
    y = house_size*0.11

    for line in matrix:
        x = house_size*0.32
        for number in range(0,10):
            text = font_mono.render(str(number), True, 'white')
            surface.blit(text, (x, y))
            x += house_size
        y += house_size