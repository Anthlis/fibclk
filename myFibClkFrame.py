import pygame, sys
from pygame.locals import *
import time

def time_is_now():
    now = time.localtime()
    hour = now.tm_hour
    min = now.tm_min
    sec = now.tm_sec

    return hour, min, sec


def square_colour(testdict):
    '''
        This creates a dictionary so that blah blah blah
    '''
    colour_dict = {
        0 : ['0', '0', '0', '0', '0'],
        1 : ['0', '0', '0', '0', '1'],
        2 : ['0', '0', '0', '1', '1'],
        3 : ['0', '0', '1', '1', '0'],
        4 : ['0', '0', '1', '1', '1'],
        5 : ['0', '1', '1', '0', '0'],
        6 : ['0', '1', '1', '1', '0'],
        7 : ['0', '1', '1', '1', '1'],
        8 : ['1', '1', '0', '0', '0'],
        9 : ['1', '1', '0', '1', '0'],
        10 : ['1', '1', '1', '0', '0'],
        11 : ['1', '1', '1', '1', '0'],
        12 : ['1', '1', '1', '1', '1']
    }
    return colour_dict.values(testdict)


def and_gate(hour_colour, min_colour):
    if (hour_colour == '0') and (min_colour == '0'):
        return white  # OFF
    elif (hour_colour == '0') and (min_colour == '1'):
        return blue   # MINS only
    elif (hour_colour == '1') and (min_colour == '0'):
        return red    # HRS only
    else:
        return green  # HRS + MINS



def main():
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0, 125)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)

    pygame.init()

    window = pygame.display.set_mode((415, 265))
    pygame.display.set_caption("Anthony's Fibonacci Clock Project")

    testdict = input("number between 0 & 12")
    testdict = square_colour()
    print(testdict)


    while True:

        # pygame to draw the black border and coloured shapes
        pygame.draw.rect(window, black, [0, 0, 5, 265])
        pygame.draw.rect(window, black, [5, 0, 415, 5])
        pygame.draw.rect(window, yellow, [5, 5, 100, 105])  # yellow 2 box
        pygame.draw.rect(window, black, [105, 5, 5, 105])
        pygame.draw.rect(window, blue, [110, 5, 50, 50])  # blue upper 1 box
        pygame.draw.rect(window, black, [110, 55, 50, 5])
        pygame.draw.rect(window, black, [5, 110, 160, 5])
        pygame.draw.rect(window, white, [5, 115, 155, 150])  # white 3 box
        pygame.draw.rect(window, green, [110, 60, 50, 50])  # green lower 1 box
        pygame.draw.rect(window, black, [5, 260, 415, 5])
        pygame.draw.rect(window, black, [160, 5, 5, 400])
        pygame.draw.rect(window, blue, [165, 5, 250, 255])  # red 5 box
        pygame.draw.rect(window, red, [165, 5, 250, 255])
        pygame.draw.rect(window, black, [410, 5, 5, 405])


        # pygame Blit the time onto the Fib Clk Frame: 5 value square
        hour, min, sec = time_is_now()
        time = str("{0:02d}:{1:02d}:{2:02d} ".format(hour, min, sec))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(time, True, black, white)
        window.blit(text, (225, 110))

        pygame.display.update()

        # Method of neatly closing down pygame window by pressing on the red 'X'
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
