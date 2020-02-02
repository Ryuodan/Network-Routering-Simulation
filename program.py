import pygame
from itemFactory import ItemFactory


BLACK=(0,0,0)
WHITE=(255,255,255)
class Program:
    all_sprites=pygame.sprite.Group()
    all_routers=[]
    all_lines=[]
    selected=None
    def __init__(self,screen, bkcolor, font):
        self.bkcolor=bkcolor
        self.screen=screen

        self.factory_width=100
        self.factory_height=screen.get_size()[1]

        self.draw_window_width=screen.get_size()[0]-self.factory_width
        self.draw_window_height=screen.get_size()[1]

        self.router_img_path='sprites/router50.png'
        self.line_img_path='sprites/line.png'
        self.djistr_img='sprites/dijkstra_img.png'
        self.delete_img='sprites/delete.png'

        self.itemFactory=ItemFactory(font=font,screen=self.screen,shelf_color=BLACK,
                        shelf_width=self.factory_width,shelf_height=self.factory_height,
                        draw_color=WHITE,draw_width=self.draw_window_width,
                        draw_height=self.draw_window_height,router_img=self.router_img_path,
                        line_img=self.line_img_path,line_color=BLACK,dijk_img=self.djistr_img,
                        delete_img=self.delete_img)


    def update_event(self,event):
        self.itemFactory.update_event(event)

    def update(self):
        self.screen.fill(self.bkcolor)
        self.itemFactory.update()
        self.all_sprites.draw(self.screen)
        for router in self.all_routers:
            self.screen.blit(router.font_renderer,dest=(router.pos_x+25,router.pos_y-2))
        for line in self.all_lines:
            line.draw(self.screen)

