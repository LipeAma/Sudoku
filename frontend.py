import pygame as pg
from math import floor
                
deafult_pallete = {
    'odd_quadrants':'#282f2a', 'even_quadrants':'#424f48', 'lines':'#566d5d', 'outline_color':'#566d5d', 'selected':'#779d82', 'number_color':'#6c7f76', 'start_color':'#65cc85', 'wrong_color1':'#d54f4f', 'wrong_color2':'#d54f4f'}

def draw_board(surface, rect, game, selected, color = deafult_pallete):
    try: board = surface.subsurface(rect)
    except: board = surface.subsurface(pg.Rect(0,0,0,0))
    draw_quadrants(board, color['odd_quadrants'], color['even_quadrants'])
    draw_selected(board, selected, color['selected'])
    draw_numbers(board, game, color['wrong_color1'], color['wrong_color2'], color['start_color'], color['number_color'])
    draw_lines(board, color['lines'])
    draw_outline(surface, rect, color['outline_color'])

def draw_quadrants(surface, odd_color, even_color):
    board_size = surface.get_width()
    quadrant_size = board_size/3
    board_rect = pg.Rect(0, 0, board_size, board_size)
    pg.draw.rect(surface, odd_color, board_rect)
    corner_list = [(1,0), (0,1), (2,1), (1,2)]
    for corners in corner_list:
        a, b = corners
        quadrant_rect = pg.Rect(quadrant_size*a, quadrant_size*b, quadrant_size+1, quadrant_size+1)
        pg.draw.rect(surface, even_color, quadrant_rect)

def draw_selected(surface, selected, color):
    board_size = surface.get_width()
    house_size = board_size/9
    m, n = selected
    hover_rect = pg.Rect(n*house_size, m*house_size, house_size+1, house_size+1)
    pg.draw.rect(surface, color, hover_rect)

def draw_numbers(surface, game, wrong_color1, wrong_color2, blocked_color, number_color):
    house_size = surface.get_width()/9
    font_mono = pg.font.Font('ai_writer_mono.ttf', int(house_size*0.6))
    board = game.get_board()
    correct = game.get_correct()
    blocked = game.get_blocked()
    y = house_size*0.11
    for m in range(9):
        x = house_size*0.32
        for n in range(9):
            number = str(board[m,n])
            if number != '0':
                if blocked[m,n] == 1:
                    text = font_mono.render(number, True, blocked_color)
                    if correct[m,n] == 0: draw_blocked_wrong(surface, (m,n), wrong_color2)
                elif correct[m,n] == 0: text = font_mono.render(number, True, wrong_color1)
                else: text = font_mono.render(number, True, number_color)
                surface.blit(text, (x, y))
            x += house_size
        y += house_size

def draw_blocked_wrong(surface, pos, color):
    house_size = surface.get_width()/9
    m, n = pos
    house_rect = pg.Rect(n*house_size, m*house_size, house_size+1, house_size+1)
    pg.draw.rect(surface, color, house_rect)

def draw_lines(surface, color):
    board_size = surface.get_width()
    house_size = board_size/9
    for n in range(1,9):
        pg.draw.line(surface, color, (n*house_size, 0), (n*house_size, board_size))
        pg.draw.line(surface, color, (0, n*house_size), (board_size, n*house_size))

def draw_outline(surface, rect, color, width = 5, border_radius = 10):
    rect.inflate_ip(width, width)
    pg.draw.rect(surface, color, rect, width, border_radius)

def get_house(mouse_pos, board_rect):
    board_size = board_rect.width
    m = floor( (mouse_pos[1] - board_rect.y)*9/board_size )
    n = floor( (mouse_pos[0] - board_rect.x)*9/board_size )
    return (m,n)

def get_pressed_key(event):
    mod = event.mod
    key = event.key
    key_list = [8, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    char_string = '0123456789'
    try:
        index = key_list.index(key)
        return (char_string[index], mod)
    except ValueError: pass