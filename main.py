import pygame as pg
import numpy as np
from sudoku_functions import *


pg.init()
screen = pg.display.set_mode(size=(1280, 720), flags= pg.RESIZABLE, vsync=0)
font_mono = pg.font.Font('ai_writer_mono.ttf',300)
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill('#1f1f1f')
    draw_board(screen, 30)

    pg.display.flip()
    #clock.tick(60)  # limits FPS to 60
pg.quit()