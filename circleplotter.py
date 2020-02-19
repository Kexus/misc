import pygame as pg
import numpy as np
import math
import random


WINSIZE = [400, 400]
r = 100

def fixCoords(x, y):
    return (x+200,y+200)

def update(s, t):

    x = math.floor(math.sin(t/r) * r)
    if t%r == 0:
        update.d *= -1
    y = update.d * math.floor(math.sqrt(r**2 - x**2))
    s.set_at((x+200,y+200), (255,255,255))
    
def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    screen.fill((0,0,0))
    
    pg.display.set_caption("Ant")
    n = 0
    done = 0
    update.d = -1
    while not done:
        update(screen, n)
        n += 1
        pg.display.update()
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = 1
                break

        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main()