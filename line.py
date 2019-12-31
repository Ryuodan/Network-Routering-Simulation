import pygame

class Line:
    
    def __init__(self,color,weigth,start_x,start_y,end_x,end_y):
        self.weigth=weigth
        self.start_x=start_x
        self.start_y=start_y
        self.end_x=end_x
        self.end_y=end_y
        self.color=color
        self.routerId_from=None
        self.routerId_to=None

    def connect_from(self,routerId,pos_x,pos_y):
        self.routerId_from=routerId
        self.start_x=pos_x
        self.start_y=pos_y

    def connect_to(self,routerId,pos_x,pos_y):
        self.routerId_to=routerId
        self.end_x=pos_x
        self.end_y=pos_y

    def draw(self,screen):
        if self.routerId_from is not None and self.routerId_to is not None:
            pygame.draw.line(screen,self.color,(self.start_x,self.start_y),(self.end_x,self.end_y))