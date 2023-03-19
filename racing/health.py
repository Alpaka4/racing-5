from config_3 import *
import pygame
class Health(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(BAR_FILE_NAME2).convert_alpha()
        self.image=pygame.transform.scale(image,(50,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
    def update(self):
        pass
    def draw(self):
        self.screen.blit(self.image, self.rect)
