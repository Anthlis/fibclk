import pygame, sys
from pygame.locals import *

pygame.init()
ZONE = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Game Zone')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

rx = ry = 20
rdx = rdy = 1

gx = gy = 280
gdx = gdy = -1

w = ZONE.get_rect().width - 10
h = ZONE.get_rect().height - 10

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    if ((rx + rdx) > w) or ((rx + rdx) < 10): rdx = -rdx
    if ((ry + rdy) > h) or ((ry + rdy) < 10): rdy = -rdy
    rx += rdx
    ry += rdy

    if ((gx + gdx) > w) or ((gx + gdx) < 10): gdx = -gdx
    if ((gy + gdy) > h) or ((gy + gdy) < 10): gdy = -gdy
    gx += gdx
    gy += gdy

    ZONE.fill(BLUE)

    RED_BALL = pygame.draw.circle(ZONE, RED, (rx, ry), 20)
    GREEN_BALL = pygame.draw.circle(ZONE, GREEN, (gx, gy), 20)
    if RED_BALL.colliderect(GREEN_BALL):
        gdx = 1
        rdx = -1
    pygame.display.update()
    clock.tick(100)
