from frame import *
from motion import *
import pygame
import os
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600, 600), RESIZABLE)
level = Frame('labyrinth')
level.generate()
level.display()
MG = Motion(level.structure)
BG = pygame.image.load("image/path2.jpg")

#color
white = (255,255,255)


def blit(x,y,image):
    window.blit(image,(x,y))

def createtext(text,Police):

    text1 = Police.render(text,True,white)
    return text1, text1.get_rect()

def message(text):

    GO = pygame.font.Font('BradBunR.ttf', 150)
    RG = pygame.font.Font('BradBunR.ttf', 50)

    text1, text2 = createtext(text, GO)
    text2.center = 300, 200
    window.blit(text1, text2)

    text3,text4 = createtext("play again ? press enter",RG)
    text4.center = 300,300
    window.blit(text3,text4)



def win_lose():

    if level.structure[MG.case_y][MG.case_x] == 'g':
        message("you lose")

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    pygame.display.quit()
                    os.system("python game.py")



def game_loop():

    run = True

    while run:

        pygame.time.delay(100)
        window.blit(MG.direction, (MG.x, MG.y))
        pygame.display.flip()
        window.blit(BG, (MG.x, MG.y))
        win_lose()
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

    pygame.quit()


if __name__ == "__main__":
    game_loop()
