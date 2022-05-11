"""
JetBear! The Game!
v0.1
Copyright 2021 Patrick Bruso
"""

import pygame as pg
import os

pg.display.set_caption("JetBear! The Game!")

# load assets
bg_image = pg.image.load(os.path.join('assets/images', 'bgtop.png'))
splash_image = pg.image.load(os.path.join('assets/images', 'Splash.png'))
start = pg.image.load(os.path.join('assets/images', 'start.png'))
bear_image = pg.image.load(os.path.join('assets/images', 'bear.png'))
base_image = pg.image.load(os.path.join('assets/images', 'bgbottom.png'))

#TODO: Make these ALLCAPS. Also make the image assets ALLCAPS?
# constants
width = bg_image.get_width()
height = bg_image.get_height()
FPS = 60

# set display call
win = pg.display.set_mode((width, height))


# Thoughts: How about adding a move() function
# With only one movement key (Spacebar)
# if KeyPressed is Spacebar Move Up
# else move down?
# This is similar to a game called Jetpack Joyride
# Going up would be slow, coming down would be fast
# The challenge would be to calculate the timings
class Bear(object):
    def __init__(self):
        self.image = bear_image
        self.x = width / 4
        self.y = height / 2

    def checkBorder(self):
        # logic to not increase distance if hit ground or border
        if self.x < 0:
            self.x = 0
        elif self.x > 900:
            self.x = 900

        if self.y < 0:
            self.y = 0
        elif self.y > 300:
            self.y = 300

    def key_handle(self):
        key = pg.key.get_pressed()
        dist = 4  # change if movement too slow
        if key[pg.K_DOWN]:
            self.y += dist
        elif key[pg.K_UP]:
            self.y -= dist
        elif key[pg.K_RIGHT]:
            self.x += dist
        elif key[pg.K_LEFT]:
            self.x -= dist

        self.checkBorder()
         

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Base:
    VEL = 5
    WIDTH = base_image.get_width()
    IMG = base_image

    def __init__(self):
        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH
        self.vel = 0

    def move(self, vel = VEL):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if(self.x1 + self.WIDTH < 0):
            self.x1 = self.x2 + self.WIDTH

        if(self.x2 + self.WIDTH < 0):
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

class Background_Top:
    VEL = 1
    WIDTH = bg_image.get_width()
    IMG = bg_image

    def __init__(self):
        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self, vel = VEL):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if(self.x1 + self.WIDTH < 0):
            self.x1 = self.x2 + self.WIDTH

        if(self.x2 + self.WIDTH < 0):
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

def main():
    """
    Main game loop that implements splash screen and calls game function upon button click
    """
    win.blit(splash_image, (0, 0))
    button = win.blit(start, (width / 2.60, height / 1.75))
    clock = pg.time.Clock()
    bear = Bear()
    base = Base()
    bgtop = Background_Top();

    isRunning = True
    isStartPressed = False
    while isRunning:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False

            #This checks if startbutton is pressed
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if button.collidepoint(pos):  
                    isStartPressed = True;

        if isStartPressed == True:
            win.blit(bg_image, (0, 0))
            bgtop.move()
            bgtop.draw(win)
            base.move()
            base.draw(win)
            bear.key_handle()
            bear.draw(win)
        else:
            #insert splash screen animation logic
            base.move(2)
            base.draw(win)
        
        pg.display.update()


    pg.quit()


if __name__ == '__main__':
    main()
