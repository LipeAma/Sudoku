import pygame as pg
import numpy as np
from frontend import *
from backend import *

pg.init()
screen = pg.display.set_mode(size=(700, 700), flags= pg.RESIZABLE)

clock = pg.time.Clock()
mouse_pos = np.array([0,0])
selected = [9,9]

board_margin = 30
running = True
game = Game('405001068073628500009003070240790030006102005950000021507064213080217050612300007')

while running:
    pressed_key = None
    
    #section to create a rectangle for the board
    display_size = pg.display.get_window_size()
    if display_size[1] < 300: pg.display.set_mode(size=(display_size[0], 300), flags= pg.RESIZABLE, depth=8, vsync=0)
    elif display_size[0] < 300: pg.display.set_mode(size=(300, display_size[1]), flags= pg.RESIZABLE, depth=8, vsync=0)
    if display_size[0] > display_size[1]: board_size = display_size[1] - 2*board_margin
    else : board_size = display_size[0] - 2*board_margin
    board_corner = ((display_size[0]-board_size)/2,(display_size[1]-board_size)/2)
    board_rect = pg.Rect(board_corner[0], board_corner[1], board_size, board_size)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        elif event.type == pg.MOUSEMOTION:
            mouse_pos = np.array(event.__dict__['pos'])
        elif event.type == pg.MOUSEBUTTONDOWN:
            selected = get_house(mouse_pos, board_rect)
        elif event.type == pg.KEYDOWN:
            pressed_key = get_pressed_key(event)
    if pressed_key is not None: game.update_game(pressed_key, selected)

    screen.fill('#111312')    
    draw_board(screen, board_rect, game, selected)
          
    pg.display.flip()
    clock.tick(30)
pg.quit()

