from frame import *
from motion import *
from write import *
import os
from pygame.locals import *


class Init:
    pygame.init()
    window = pygame.display.set_mode()
    level = Frame('labyrinth.txt')
    level.generate()
    level.display()
    list = level.items(window)
    MG = Motion(level.structure)
    BG = pygame.image.load("image/path2.jpg")
    item = pygame.image.load("image/loot.png")
    state = [False, False, False]


def check():
    mg_pos = (Init.MG.x, Init.MG.y)

    if Init.list[0] == mg_pos:
        Init.state[0] = True
        Init.window.blit(Init.item, (150, 460))

    if Init.list[1] == mg_pos:
        Init.state[1] = True
        Init.window.blit(Init.item, (200, 460))

    if Init.list[2] == mg_pos:
        Init.state[2] = True
        Init.window.blit(Init.item, (250, 460))

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
    write = Write()
    if Init.level.structure[Init.MG.case_y][Init.MG.case_x] == 'g' and check():
        write.message("you win")
        replay()

    if Init.level.structure[Init.MG.case_y][Init.MG.case_x] == 'g' and not check():
        write.message("you lose")
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
