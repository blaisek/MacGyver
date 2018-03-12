import pygame
from pygame.locals import *


class Motion:

    def __init__(self, frame):

        self.pic = pygame.image.load('Macgyver.png')
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.direction = self.pic
        self.frame = frame

    def move(self, direction):

        size = 30
        if direction == 'right':
            if self.case_x < 14:
                if self.frame[self.case_y][self.case_x+1] != '#':
                    self.case_x +=1
                    self.x = self.case_x * size
                self.direction = self.pic

        if direction == 'left':
            if self.case_x > 0:
                if self.frame[self.case_y][self.case_x-1] != '#':
                    self.case_x -= 1
                    self.x = self.case_x * size
                self.direction = self.pic

        if direction == 'up':
            if self.case_y > 0:
                if self.frame[self.case_y-1][self.case_x] != '#':
                    self.case_y -= 1
                    self.y = self.case_y * size
                self.direction = self.pic

        if direction == 'down':
            if self.case_y < 14:
                if self.frame[self.case_y+1][self.case_x] != '#':
                    self.case_y += 1
                    self.y = self.case_y * size
            self.direction = self.pic


