import pygame
from pygame.locals import *
import random


class Frame:

    def __init__(self, file):
        self.file = file
        self.structure = []
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.size = 30

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
                x = x_case * self.size
                y = y_case * self.size
                if sprite == '#':
                    window.blit(wall, (x, y))
                elif sprite == 'g':
                    window.blit(guard, (x, y))
                x_case += 1
            y_case += 1

    def items(self, window):

        items = pygame.image.load("image/loot.png")
        x = random.randrange(15)
        y = random.randrange(15)
        rand_x = x * self.size
        rand_y = y * self.size

        for line in self.structure:

            if self.structure[y][x] != '#' and self.structure[y][x] == '0':
                
                    window.blit(items, (rand_x, rand_y))

            else:
                x = random.randrange(15)
                y = random.randrange(15)







