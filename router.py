import pygame

class Router(pygame.sprite.Sprite):
    image = pygame.image.load('sprites/router50.png')
    print(f'size of router img {image.get_size()}')
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect((pos_x,pos_y), Router.image.get_size())
        self.y=0

    