from frame import *
from motion import *
import pygame
from pygame.locals import *


pygame.init()
window = pygame.display.set_mode((600, 600), RESIZABLE)
level = Frame('labyrinth')
level.generate()
level.display()
MG = Motion(level.structure)
BG = pygame.image.load("BG.png")


def win_lose():

    x = MG.x
    y = MG.y
    for line in level.structure:

        for sprite in line:
            if sprite == 'g':
                if x == level.x and y == level.y:
                    print("You win")


def gameloop():

    run = True

    while run:

        pygame.time.delay(100)
        window.blit(MG.direction, (MG.x, MG.y))
        pygame.display.flip()
        window.blit(BG,(MG.x,MG.y))

        for event in pygame.event.get():

            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == K_RIGHT:
                    MG.move('right')
                elif event.key == K_LEFT:
                    MG.move('left')
                elif event.key == K_UP:
                    MG.move('up')
                elif event.key == K_DOWN:
                    MG.move('down')
            win_lose()
    pygame.quit()

if __name__ == "__main__":
    gameloop()