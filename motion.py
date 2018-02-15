from frame import *
import pygame
from pygame.locals import *




class Motion:



    def __init__(self,picture):

        self.picture = pygame.image.load(picture)
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0


    def move(self,direction):

        size = 30
        if direction == 'right':
            if Frame.structure[self.case_y][self.case_x+1] != '#':
                self.case_x +=1
                self.x = self.case_x * size
            self.direction = self.picture

        if direction == 'left':
            if Frame.structure[self.case_y][self.case_x-1] != '#':
                self.case_x -=1
                self.x = self.case_x * size
            self.direction = self.picture

        if direction == 'up':
            if Frame.structure[self.case_y-1][self.case_x] != '#':
                self.case_y -=1
                self.y = self.case_y * size
            self.direction = self.picture

        if direction == 'down':
            if Frame.structure[self.case_y+1][self.case_x] != '#':
                self.case_y +=1
                self.y = self.case_y * size
            self.direction = self.picture

