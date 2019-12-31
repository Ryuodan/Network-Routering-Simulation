import pygame

BLUE=(0,0,255)
class Line:
    
    def __init__(self,color,font,start_x,start_y,end_x,end_y):
        self.weight=0
        self.font=font
        self.start_x=start_x
        self.start_y=start_y
        self.end_x=end_x
        self.end_y=end_y
        self.color=color
        self.routerId_from=None
        self.routerId_to=None

        self.weight_text =None

    def connect_from(self,routerId,pos_x,pos_y):
        self.routerId_from=routerId
        self.start_x=pos_x
        self.start_y=pos_y

    def connect_to(self,routerId,pos_x,pos_y):
        self.routerId_to=routerId
        self.end_x=pos_x
        self.end_y=pos_y

    def set_weight(self,weight):
        self.weight=weight
        self.weight_text=self.font.render(str(weight), True, BLUE)

    def draw(self,screen):
        if self.routerId_from is not None and self.routerId_to is not None:
            pygame.draw.line(screen,self.color,(self.start_x,self.start_y),(self.end_x,self.end_y))
            if self.end_x>self.start_x:
                x_pos=self.start_x+(self.end_x-self.start_x)/2
            else:
                x_pos=self.end_x+(self.start_x-self.end_x)/2

            if self.end_y > self.start_y:
                y_pos=self.start_y+(self.end_y-self.start_y)/2
            else:
                y_pos=self.end_y+(self.start_y-self.end_y)/2
            screen.blit(self.weight_text,dest=(x_pos,y_pos))