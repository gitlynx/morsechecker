# Simple morse checker

# Used references
#   https://pygamewidgets.readthedocs.io/en/latest/widgets/progressbar/
#   https://pygamewidgets.readthedocs.io/en/latest/widgets/slider/

"""
    This is a simple visual representation of morse code linked to an 
    (external) input. Showing the dots and dashes.

    from https://en.wikipedia.org/wiki/Morse_code:
    A morse code symbol consists of 'dits' and 'dahs'. The dit duration can
    vary for signal clarity and operator skills, but it's the basic unit
    of time measurement.

    - A 'dah' is minimal 3 times the duration of a 'dit'.
    - There's minimal 1 'dit' space between consecutive 'dits' and 'dahs' to 
      separate morse symbols
    - There is minimal 3 'dit' space between letters.
    - There is minimal 7 'dit' space between words.
"""



import pygame_widgets
import pygame
import time

from morse_data import Morse


DISPLAY_COLOR = (0, 0, 0)
COLOR_ON = (0, 255, 0)
COLOR_OFF = (255, 0, 0)
TEXT_COLOR = (255, 0, 255)
BACKGROUND_COLOR = DISPLAY_COLOR


def morse_grid(surface: pygame.Surface) -> ():
    '''
        Calculate the morse grid.

        Worst case morse symbol is 0 (5 x dah)
        Leading 12 dit space
    '''
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


def render_symbol(surface: pygame.Surface, character):
    '''
        Show the morse symbol as character

        Reference: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
    '''
    if character is not None:
        surface_rect = surface.get_rect()
        font = pygame.font.Font('freesansbold.ttf', 128)
        text = font.render(character, True, TEXT_COLOR, BACKGROUND_COLOR)
        textRect = text.get_rect()
        textRect.center = (surface_rect.width // 2, 200)

        surface.blit(text, textRect)



def render_reference(surface: pygame.Surface, dits_array, y_offset, character = None):
    '''
        Render a dits reference and morse pattern
    '''
    dit_pattern = [False for element in range(32)]

    if character is not None and character in Morse.morse_dict:
        morse_pattern = Morse.morse_dict[character]
        for i in range(len(morse_pattern)):
            dit_pattern[i + 12] = True if morse_pattern[i] is True else False

    for dit in dits_array:
        if character is not None and character in Morse.morse_dict:
            pattern_index = dits_array.index(dit)
            rec_width = 0 if dit_pattern[pattern_index] is True else 2
        else:
            rec_width = 2

        pygame.draw.rect(surface, (176, 176, 176), dit.move(0, y_offset), border_radius=3, width=rec_width)

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
    morse_symbol = None

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
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if not keys[pygame.K_SPACE]:
                    user_text = event.unicode
                    if len(user_text):
                        morse_symbol = user_text[0].lower()

        keys_pressed = pygame.key.get_pressed()
        paddle_press = keys_pressed[pygame.K_SPACE]

        if render_marker(win, 60, startTime, 1.0, time.time(), paddle_press) is False:
            startTime = time.time()
            win.fill(DISPLAY_COLOR)
            render_reference(win, dits_array, 20, character = morse_symbol)
            render_symbol(win, morse_symbol)

    
        pygame.display.update()


if __name__ == "__main__":
    game()

