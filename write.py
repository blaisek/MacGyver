import pygame
from game import Init


class Write:
    def __init__(self):
        self.window = Init.window

    def blit(self, x, y, image):
        self.window.blit(image, (x, y))

    def createtext(self, text, Police):
        # color
        white = (255, 255, 255)
        text1 = Police.render(text, True, white)
        return text1, text1.get_rect()

    def message(self, text):
        GO = pygame.font.Font('BradBunR.ttf', 150)
        RG = pygame.font.Font('BradBunR.ttf', 50)

        text1, text2 = self.createtext(text, GO)
        text2.center = 300, 200
        self.window.blit(text1, text2)

        text3, text4 = self.createtext("play again ? press enter", RG)
        text4.center = 300, 300
        self.window.blit(text3, text4)
