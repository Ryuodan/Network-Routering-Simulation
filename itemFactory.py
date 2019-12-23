import pygame
from router import Router
import program

class ItemFactory:
    def __init__(self,screen,color,width,height,router_img):
        self.router_image_obj = pygame.image.load(router_img)
        self.background_img = pygame.Surface([width, height])
        pygame.draw.rect(self.background_img, color, [0, 0, width, height]) 
        self.screen=screen

    def button(self,img,pos_x,pos_y,size,item_type,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.screen.blit(img,(pos_x,pos_y))
        width,height=size
        if pos_x+width > mouse[0] > pos_x and pos_y+height > mouse[1] > pos_y:
            if click[0] == 1 and action != None:
                print('dost 3lya')
                obj=action(200,200)
                if item_type=='Router':
                    program.Program.all_routers.append(obj)
                program.Program.all_sprites.add(obj)
    
    def create_router(self,pos_x,pos_y):
        router_obj=Router(self.router_image_obj,pos_x,pos_y)
        print('ana at3mlt router')
        return router_obj


    def create_line(self,pos_x,pos_y):
        pass
    
    def update(self):
        self.screen.blit(self.background_img, (0,0))
        self.button(self.router_image_obj,25,50,self.router_image_obj.get_size(),
            item_type='Router',action=self.create_router)