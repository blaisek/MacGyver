import pygame
from pygame.locals import *



class Frame :

    def __init__(self,file):
        self.file = file
        self.structure = 0

    def generate(self):

        with open(self.file,"r") as file:
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
        pers = pygame.image.load("Macgyver.png")
        guard = pygame.image.load('guard.png')
        wall = pygame.image.load('wall.png')
        window = pygame.display.set_mode((500, 480), RESIZABLE)
        pygame.display.set_caption("MacGyver")
        y_case = 0
        for line in self.structure:
            x_case = 0
            for sprite in line:
                x = x_case *size
                y = y_case *size
                if sprite == '#':
                    window.blit(wall,(x,y))
                elif sprite == 'M':
                    window.blit(pers,(x,y))
                elif sprite == 'g':
                    window.blit(guard,(x,y))
                x_case +=1
            y_case +=1



