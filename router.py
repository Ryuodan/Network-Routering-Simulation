import pygame

class Router(pygame.sprite.Sprite):

    def __init__(self,img,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect = pygame.Rect((pos_x,pos_y), img.get_size())
        self.y=0
    
    