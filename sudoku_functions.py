import pygame


def draw_board(surface, margin):
    (width, height) = surface.get_size()
    if height > width: side_length = width-2*margin
    else : side_length = height-2*margin
    corners = (x,y) = ((width-side_length)/2,(height-side_length)/2)
    
    house_length = round(side_length/9, 0)
    for n in [1,2,4,5,7,8]:
        pygame.draw.line(surface, '#949494', (x+n*house_length,y), (x+n*house_length,y+side_length-2)) # subtracting 2 pixels to prevent leaving the frame
        pygame.draw.line(surface, '#949494', (x,y+n*house_length), (x+side_length-2,y+n*house_length)) # subtracting 2 pixels to prevent leaving the frame

    quadrant_length = side_length/3
    for n in [1,2]:
        pygame.draw.line(surface, '#c7c7c7', (x+n*quadrant_length,y), (x+n*quadrant_length,y+side_length-2),3) # subtracting 2 pixels to prevent leaving the frame
        pygame.draw.line(surface, '#c7c7c7', (x,y+n*quadrant_length), (x+side_length-2,y+n*quadrant_length),3) # subtracting 2 pixels to prevent leaving the frame

    frame = pygame.Rect( x, y, side_length, side_length)
    pygame.draw.rect(surface, '#d5d5d5', frame, width=6, border_radius=40)


#def draw_numbers(surface, margin, )