from config_3 import *
import pygame
import random
class Bar(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BAR_FILE_NAME).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.image=pygame.transform.scale(self.image,(80,100))
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.speedy=10
    def update(self):
        self.rect.y+=self.speedy
    def draw(self):
        self.screen.blit(self.image, self.rect)
