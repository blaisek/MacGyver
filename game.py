from frame import *
from motion import *
import pygame
from pygame.locals import *


pygame.init()

level = Frame('labyrinth')
level.generate()
level.display()
mac = Motion('Macgyver.png')
pers = pygame.image.load('Macgyver.png')


def gameloop():

    run = 1

    while run:

        pygame.display.flip()
        #pygame.Surface.blit(pers,(mac.x,mac.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                run = 0
            elif event.type == K_RIGHT:
                mac.move('right')
            elif event.type == K_LEFT:
                mac.move('left')
            elif event.type == K_UP:
                mac.move('up')
            elif event.type == K_DOWN:
                mac.move('down')





gameloop()