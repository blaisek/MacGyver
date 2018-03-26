from frame import *
from motion import *
import pygame
import os
from pygame.locals import *


class Init:
    pygame.init()
    window = pygame.display.set_mode((400, 400), RESIZABLE)
    level = Frame('labyrinth.txt')
    level.generate()
    level.display()
    list = level.items(window)
    MG = Motion(level.structure)
    BG = pygame.image.load("image/path2.jpg")
    item = pygame.image.load("image/loot.png")
    state = [False, False, False]


def blit(x, y, image):
    Init.window.blit(image, (x, y))


def createtext(text, Police):
    # color
    white = (255, 255, 255)
    text1 = Police.render(text, True, white)
    return text1, text1.get_rect()


def message(text):
    GO = pygame.font.Font('BradBunR.ttf', 150)
    RG = pygame.font.Font('BradBunR.ttf', 50)

    text1, text2 = createtext(text, GO)
    text2.center = 300, 200
    Init.window.blit(text1, text2)

    text3, text4 = createtext("play again ? press enter", RG)
    text4.center = 300, 300
    Init.window.blit(text3, text4)

def check():

    mg_pos = (Init.MG.x, Init.MG.y)

    if Init.list[0] == mg_pos:
        Init.state[0] = True
        Init.window.blit(Init.item, (200, 515))

    if Init.list[1] == mg_pos:
        Init.state[1] = True
        Init.window.blit(Init.item, (250, 515))

    if Init.list[2] == mg_pos:
        Init.state[2] = True
        Init.window.blit(Init.item, (300, 515))

    return Init.state[0] and Init.state[1] and Init.state[2]


def replay():
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                pygame.display.quit()
                os.system("python game.py")


def win_lose():
    if Init.level.structure[Init.MG.case_y][Init.MG.case_x] == 'g' and check():
        message("You Win")
        replay()

    if Init.level.structure[Init.MG.case_y][Init.MG.case_x] == 'g' and not check():
        message("You lose")
        replay()


def game_loop():
    run = True
    while run:

        pygame.time.delay(100)
        Init.window.blit(Init.MG.direction, (Init.MG.x, Init.MG.y))
        pygame.display.flip()
        Init.window.blit(Init.BG, (Init.MG.x, Init.MG.y))
        check()
        win_lose()
        for event in pygame.event.get():

            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == K_RIGHT:
                    Init.MG.move('right')
                elif event.key == K_LEFT:
                    Init.MG.move('left')
                elif event.key == K_UP:
                    Init.MG.move('up')
                elif event.key == K_DOWN:
                    Init.MG.move('down')

    pygame.quit()


if __name__ == "__main__":
    game_loop()

