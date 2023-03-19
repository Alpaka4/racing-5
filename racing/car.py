from config_3 import *
import pygame
class Car(pygame.sprite.Sprite):
    def __init__(self,filename, screen,x,y):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=(400,SCREEN_HEIGHT//2))
        self.speedx=0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx+=-1
        elif keys[pygame.K_d]:
            self.speedx+=1
        else:
            self.speedx=0
        self.rect.x+=self.speedx
        if self.rect.right>RIGHT_BORDER:
            self.rect.right=RIGHT_BORDER
        if self.rect.left<LEFT_BORDER:
            self.rect.left=LEFT_BORDER
    def draw(self):
        self.screen.blit(self.image, self.rect)
