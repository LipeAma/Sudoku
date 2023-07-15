import pygame as pg
import numpy as np
from sudoku_board import *
from sudoku_code import *


pg.init()
screen = pg.display.set_mode(size=(1280, 720), flags= pg.RESIZABLE, depth=8, vsync=0)
clock = pygame.time.Clock()
mouse_pos = np.array([0,0])
running = True
game = Game('070000043040009610800634900094052000358460020000800530080070091902100005007040802')

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        elif event.type == pg.MOUSEMOTION:
            mouse_pos = np.array(event.__dict__['pos'])

    display_size = pg.display.get_window_size()
    
    # section to prevent the board from beeing to big
    board_margin = 30
    if display_size[0] > display_size[1]: board_size = display_size[1] - 2*board_margin
    else : board_size = display_size[0] - 2*board_margin
    board_corner = ((display_size[0]-board_size)/2,(display_size[1]-board_size)/2)
   

    board_rect = pygame.Rect(board_corner[0], board_corner[1], board_size, board_size)
    board = screen.subsurface(board_rect)
    board.fill((0,0,0,0))
    screen.fill('#1d201d')
    
    

    draw_quadrants(board)
    highlight_hovered(board, mouse_pos)
    draw_lines(board)
    board_rect.inflate_ip(6,6)
    pygame.draw.rect(screen, '#6e8270', board_rect, width=4, border_radius=10)
    draw_numbers(board, game.board)
            
    pg.display.flip()
    clock.tick(30)
pg.quit()

