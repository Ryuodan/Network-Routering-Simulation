import pygame

class Router(pygame.sprite.Sprite):
    counter=1000
    def __init__(self,img,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.rect = pygame.Rect((pos_x,pos_y), img.get_size())
        self.y=0
        self.id=Router.counter
        Router.counter+=1
    