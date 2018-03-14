import pygame
from pygame.locals import *


class Frame:

    def __init__(self, file):
        self.file = file
        self.structure = []
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def generate(self):

        with open(self.file, "r") as file:
            file_structure = []
            for line in file:
                nbr_line = []
                for sprite in line:
                    if sprite != '\n':
                        nbr_line.append(sprite)
                file_structure.append(nbr_line)
            self.structure = file_structure

    def display(self):

        size = 30

        guard = pygame.image.load('image/guard.png')
        wall = pygame.image.load('image/wall2.png')
        background = pygame.image.load("image/background.jpg")
        window = pygame.display.set_mode((600, 600), RESIZABLE)
        window.blit(background, (0, 0))
        pygame.display.set_caption("MacGyver")

        y_case = 0
        for line in self.structure:
            x_case = 0
            for sprite in line:
                x = x_case * size
                y = y_case * size
                if sprite == '#':
                    window.blit(wall, (x, y))
                elif sprite == 'g':
                    window.blit(guard, (x, y))
                x_case += 1
            y_case += 1






