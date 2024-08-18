# Simple morse checker

# Used references
#   https://pygamewidgets.readthedocs.io/en/latest/widgets/progressbar/
#   https://pygamewidgets.readthedocs.io/en/latest/widgets/slider/




import pygame_widgets
import pygame
import time

from morse_data import Morse


DISPLAY_COLOR = (0, 0, 0)
COLOR_ON = (0, 255, 0)
COLOR_OFF = (255, 0, 0)


def morse_grid(surface: pygame.Surface) -> ():
    surface_rect = surface.get_rect()

    dit_width = surface_rect.width // 33
    dit_offset = dit_width // 2

    dit_top = surface_rect.top
    dit_height = 30

    dits_array = []
    for i in range(32):
        left = dit_offset + i * dit_width
        dits_array.append(pygame.Rect(left, dit_top, dit_width, dit_height))

    return dits_array


def render_reference(surface: pygame.Surface, dits_array, y_offset, character = None):

    for dit in dits_array:
        pygame.draw.rect(surface, (176, 176, 176), dit.move(0, y_offset), border_radius=3, width=2)

def render_marker(surface: pygame.Surface, y_offset, startTime, maxTime, current_time, on: bool) -> bool:
    '''
      Draw a marker
    '''
    surface_rect = surface.get_rect()
    x_offset = (surface_rect.width // 33) // 2
    dits_width =  (32 * (surface_rect.width // 33))
    x_max = x_offset + dits_width
    x = x_offset + ((time.time() - startTime) * 100 // maxTime)
    if ( x < x_max):
        line_color = COLOR_ON if on is True else COLOR_OFF
        pygame.draw.line(surface, line_color, (x, y_offset), (x, y_offset + 20), width = 1)
        return True

    return False

def game():
    #Pygame setup
    pygame.init()
    win = pygame.display.set_mode((1000,600))


    startTime = time.time()


    dits_array = morse_grid(win)
    render_reference(win, dits_array, 20)

    pygame.display.flip()


    run = True
    while run:
        paddle_press = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
#            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                paddle_press = True

        keys_pressed = pygame.key.get_pressed()
        paddle_press = keys_pressed[pygame.K_SPACE]

        if render_marker(win, 60, startTime, 1.0, time.time(), paddle_press) is False:
            startTime = time.time()
            win.fill(DISPLAY_COLOR)
            render_reference(win, dits_array, 20)

    
        pygame.display.update()


if __name__ == "__main__":
    game()

