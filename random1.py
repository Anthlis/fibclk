import pygame, sys
from pygame.locals import *
import datetime
import random


def main():
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0, 125)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    orange = (255, 128, 0)

    colours = [white, red, blue, green, yellow, orange]

    pygame.init()

    window = pygame.display.set_mode((415, 265))
    pygame.display.set_caption("Anthony's Fibonacci Clock Project")

    running = True

    pygame.draw.rect(window, black, [0, 0, 5, 265])
    pygame.draw.rect(window, black, [5, 0, 415, 5])
    pygame.draw.rect(window, random.choice(colours), [5, 5, 100, 105])  # yellow 2 box
    pygame.draw.rect(window, black, [105, 5, 5, 105])
    pygame.draw.rect(window, random.choice(colours), [110, 5, 50, 50])  # blue upper 1 box
    pygame.draw.rect(window, black, [110, 55, 50, 5])
    pygame.draw.rect(window, black, [5, 110, 160, 5])
    pygame.draw.rect(window, random.choice(colours), [5, 115, 155, 150])  # white 3 box
    pygame.draw.rect(window, random.choice(colours), [110, 60, 50, 50])  # green lower 1 box
    pygame.draw.rect(window, black, [5, 260, 415, 5])
    pygame.draw.rect(window, black, [160, 5, 5, 400])
    pygame.draw.rect(window, random.choice(colours), [165, 5, 250, 255])  # red 5 box
    # pygame.draw.rect(window, random.choice(colours), [165, 5, 250, 255])
    pygame.draw.rect(window, black, [410, 5, 5, 405])

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:


                pygame.draw.rect(window, black, [0, 0, 5, 265])
                pygame.draw.rect(window, black, [5, 0, 415, 5])
                pygame.draw.rect(window, random.choice(colours), [5, 5, 100, 105])  # yellow 2 box
                pygame.draw.rect(window, black, [105, 5, 5, 105])
                pygame.draw.rect(window, random.choice(colours), [110, 5, 50, 50])  # blue upper 1 box
                pygame.draw.rect(window, black, [110, 55, 50, 5])
                pygame.draw.rect(window, black, [5, 110, 160, 5])
                pygame.draw.rect(window, random.choice(colours), [5, 115, 155, 150])  # white 3 box
                pygame.draw.rect(window, random.choice(colours), [110, 60, 50, 50])  # green lower 1 box
                pygame.draw.rect(window, black, [5, 260, 415, 5])
                pygame.draw.rect(window, black, [160, 5, 5, 400])
                pygame.draw.rect(window, random.choice(colours), [165, 5, 250, 255])  # red 5 box
                #pygame.draw.rect(window, random.choice(colours), [165, 5, 250, 255])
                pygame.draw.rect(window, black, [410, 5, 5, 405])


            elif event.type == pygame.MOUSEBUTTONUP:

                pygame.draw.rect(window, black, [0, 0, 5, 265])
                pygame.draw.rect(window, black, [5, 0, 415, 5])
                pygame.draw.rect(window, random.choice(colours), [5, 5, 100, 105])  # yellow 2 box
                pygame.draw.rect(window, black, [105, 5, 5, 105])
                pygame.draw.rect(window, random.choice(colours), [110, 5, 50, 50])  # blue upper 1 box
                pygame.draw.rect(window, black, [110, 55, 50, 5])
                pygame.draw.rect(window, black, [5, 110, 160, 5])
                pygame.draw.rect(window, random.choice(colours), [5, 115, 155, 150])  # white 3 box
                pygame.draw.rect(window, random.choice(colours), [110, 60, 50, 50])  # green lower 1 box
                pygame.draw.rect(window, black, [5, 260, 415, 5])
                pygame.draw.rect(window, black, [160, 5, 5, 400])
                pygame.draw.rect(window, random.choice(colours), [165, 5, 250, 255])  # red 5 box
                # pygame.draw.rect(window, random.choice(colours), [165, 5, 250, 255])
                pygame.draw.rect(window, black, [410, 5, 5, 405])


            pygame.display.flip()


        # window.fill(white) # commented out because the frame and boxes fill the window screen.
'''
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

        # get the current time
        now = datetime.datetime.now()
        timenow = str(datetime.time(now.hour, now.minute, now.second))

        # pygame Blit the time onto the Fib Clk Frame
        FONT = pygame.font.Font('freesansbold.ttf', 32)
        TEXT = FONT.render(timenow, True, black, white)
        window.blit(TEXT, (225, 110))
'''
        #pygame.display.flip()



'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
'''

if __name__ == '__main__':
    main()
