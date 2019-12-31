import pygame
BLUE=(0,255,0)
class Router(pygame.sprite.Sprite):
    counter=0
    def __init__(self,img,font,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.rect = pygame.Rect((pos_x,pos_y), img.get_size())
        self.y=0
        Router.counter+=1
        self.id='R'+str(Router.counter)
        self.font_renderer=font.render(self.id, True, BLUE)