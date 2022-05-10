"""
JetBear! The Game!
v0.1
Copyright 2021 Patrick Bruso
"""

import pygame as pg
import os

pg.display.set_caption("JetBear! The Game!")

# load assets
bg_image = pg.image.load(os.path.join('assets/images', 'background_wide.png'))
splash_image = pg.image.load(os.path.join('assets/images', 'Splash.png'))
start = pg.image.load(os.path.join('assets/images', 'start.png'))
bear_image = pg.image.load(os.path.join('assets/images', 'bear.png'))

# constants
width = bg_image.get_width()
height = bg_image.get_height()
FPS = 60

# set display call
win = pg.display.set_mode((width, height))


class Bear(object):
    def __init__(self):
        self.image = bear_image
        self.x = width / 4
        self.y = height / 2

    def key_handle(self):
        key = pg.key.get_pressed()
        dist = 2  # change if movement too slow
        if key[pg.K_DOWN]:
            self.y += dist
        elif key[pg.K_UP]:
            self.y -= dist
        elif key[pg.K_RIGHT]:
            self.x += dist
        elif key[pg.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        pg.display.update()  # testing update within Bear class


def main():
    """
    Main game loop that implements splash screen and calls game function upon button click
    """
    win.blit(splash_image, (0, 0))
    button = win.blit(start, (width / 2.60, height / 1.75))
    clock = pg.time.Clock()
    bear = Bear()

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if button.collidepoint(pos):
                    win.blit(bg_image, (0, 0))

        bear.draw(win)
        bear.key_handle()
        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    main()
