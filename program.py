import pygame
from itemFactory import ItemFactory

BLACK=(0,0,0)

class Program:
    all_sprites=pygame.sprite.Group()
    all_routers=[]

    def __init__(self,screen, bkcolor):
        self.bkcolor=bkcolor
        self.screen=screen
        self.factory_width=100
        self.factory_height=screen.get_size()[1]
        self.router_img_path='sprites/router50.png'
        self.line_img_path='sprites/line.png'
        self.itemFactory=ItemFactory(screen=self.screen,color=BLACK,
                        width=self.factory_width,height=self.factory_height,
                    router_img=self.router_img_path,line_img=self.line_img_path)

        self.routers=[]


    def update(self):
        self.screen.fill(self.bkcolor)
       
        self.itemFactory.update()
        self.all_sprites.draw(self.screen)

