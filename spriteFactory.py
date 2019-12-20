import pygame
from router import Router
class SpriteFactory():

    def __init__(self,screen, color, width, height):
        self.background_img = pygame.Surface([width, height])
        self.screen=screen
        self.router_image = pygame.image.load('sprites/router50.png')
        pygame.draw.rect(self.background_img, color, [0, 0, width, height])
        
        #self.rect = self.image.get_rect()

    def update(self):
        self.screen.blit(self.background_img, (0,0))
        self.screen.blit(self.router_image,(25,50))

    def create_router(self,pos_x,pos_y):
        router_obj=Router(self.router_image,pos_x,pos_y)
        return router_obj
