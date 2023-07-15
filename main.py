import pygame as pg
import numpy as np
from sudoku_functions import *


pg.init()
screen = pg.display.set_mode(size=(1280, 720), flags= pg.RESIZABLE, depth=16, vsync=0)
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
    display_size = pg.display.get_window_size()
    screen.fill('#1f1f1f')
    # section to prevent the board from beeing to big
    board_margin = 30
    if display_size[0] > display_size[1]: board_size = display_size[1] - 2*board_margin
    else : board_size = display_size[0] - 2*board_margin
    board_corner = ((display_size[0]-board_size)/2,(display_size[1]-board_size)/2)

    matrix = np.zeros((9,9)).astype(int)

    board = pg.surface.Surface((board_size, board_size)).convert_alpha()
    board.fill((0,0,0,0))
    draw_board(board)
    draw_numbers(board, matrix)
    screen.blit(board, board_corner)

    #draw board edge
    frame_width = 6
    frame = pygame.Rect(board_corner[0]-frame_width, board_corner[1]-frame_width, board_size+frame_width, board_size+frame_width)
    pygame.draw.rect(screen, '#d5d5d5', frame, width=frame_width, border_radius=10)

    pg.display.flip()
    #clock.tick(60)  # limits FPS to 60
pg.quit()