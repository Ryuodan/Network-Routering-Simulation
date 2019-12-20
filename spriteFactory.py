import pygame
from router import Router
class SpriteFactory():

    def __init__(self,screen, color, width, height):
        self.background_img = pygame.Surface([width, height])
        self.screen=screen
        self.router_image = pygame.image.load('sprites/router50.png')
        #self.router_button=
        pygame.draw.rect(self.background_img, color, [0, 0, width, height])
        #self.rect = self.image.get_rect()
        self.all_sprites=pygame.sprite.Group()

    def button(self,img,pos_x,pos_y,size,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        width,height=size
      #  print(click)
        if pos_x+width > mouse[0] > pos_x and pos_y+height > mouse[1] > pos_y:
          #  pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
          #  print('enta gwa el box')
            if click[0] == 1 and action != None:
                print('dost 3lya')
                action(200,200)
                #action()         
      #  else:
      #      pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    #    smallText = pygame.font.SysFont("comicsansms",20)
     #   textSurf, textRect = text_objects(msg, smallText)
     #   textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.screen.blit(img,(pos_x,pos_y))

    def update(self):

        self.screen.blit(self.background_img, (0,0))
        self.button(self.router_image,25,50,self.router_image.get_size(),action=self.create_router)
        
        self.all_sprites.draw(self.screen)

    def create_router(self,pos_x,pos_y):
        router_obj=Router(self.router_image,pos_x,pos_y)
        print('ana at3mlt router')
        self.all_sprites.add(router_obj)
