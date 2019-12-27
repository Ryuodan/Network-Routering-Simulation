import pygame

class Line:
    
    def __init__(self,color,weigth,start_x,start_y,end_x,end_y):
        self.weigth=weigth
        self.start_x=start_x
        self.start_y=start_y
        self.end_x=end_x
        self.end_y=end_y
        self.color=color
        self.line_connected_from=None
        self.line_connected_to=None

    def connect_from(self,routerId,start_x,start_y):
        self.line_connected_from=routerId
        self.start_x=start_x
        self.start_y=start_y

    def connect_to(self,routerId,end_x,end_y):
        self.line_connected_to=routerId
        self.end_x=end_x
        self.end_y=end_y

    def draw(self,screen):
        if self.line_connected_from is not None and self.line_connected_to is not None:
            pygame.draw.line(screen,self.color,(self.start_x,self.start_y),(self.end_x,self.end_y))