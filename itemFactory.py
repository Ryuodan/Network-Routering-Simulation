import pygame
from router import Router
from line import Line
import program


class ItemFactory:
    def __init__(self,screen,shelf_color,shelf_width,shelf_height,draw_width,
                draw_height,draw_color,router_img,line_img,line_color):
        self.router_image_obj = pygame.image.load(router_img)
        self.line_image_obj = pygame.image.load(line_img)

        self.background_img = pygame.Surface([shelf_width, shelf_height])
        pygame.draw.rect(self.background_img , shelf_color, [0, 0, shelf_width, shelf_height]) 

        self.draw_img = pygame.Surface([draw_width, draw_height])
        pygame.draw.rect(self.draw_img , draw_color, [0, 0, draw_width, draw_height]) 
        
        self.background_img = pygame.Surface([shelf_width, shelf_height])
        pygame.draw.rect(self.background_img , shelf_color, [0, 0, shelf_width, shelf_height]) 

        self.line_color=line_color
        self.selected=None
        self.screen=screen
        self.event=None

        #handling variables
        self.line_first_time=True


    def button(self,img,pos_x,pos_y,size,item_type):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       # print(event)
        self.screen.blit(img,(pos_x,pos_y))
      #  print(pygame.event.get())    
        width,height=size
        if pos_x+width > mouse[0] > pos_x and pos_y+height > mouse[1] > pos_y:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            #when right clicked unselect all
            if self.event.type ==pygame.MOUSEBUTTONDOWN and self.event.button==3:
                #resest everything
                self.selected=None
                self.line_first_time=True
            #when left clicked select and do all functioanlity
            if self.event.type == pygame.MOUSEBUTTONDOWN and self.event.button == 1: #action != None:
                print('clicked')
                #ROUTER SELECTED
                if item_type=='router':
                    self.selected='router'
                #LINE SELECTED
                if item_type=='line':
                    self.selected='line'
                #DRAW WINDOW SELECTED
                if item_type=='draw':
                    #IF IT'S A ROUTER
                    if self.selected=='router':
                        if self.clicked_on_router(mouse[0],mouse[1]) is not None:
                            return None
                        router_obj=self.create_router(mouse[0],mouse[1])
                        program.Program.all_routers.append(router_obj)
                        program.Program.all_sprites.add(router_obj)
                    #IF TI'S A LINE
                    if self.selected=='line':
                        obj=self.clicked_on_router(mouse[0],mouse[1])
                        if obj is not None:
                            #CONNECT FROM
                            if self.line_first_time:
                                line=self.create_line(0,0,0,0)###you stoped here connect lines to routers 
                                line.connect_from(routerId=obj.id,start_x=mouse[0],start_y=mouse[1])
                                program.Program.all_lines.append(line)
                                self.line_first_time=False
                            #CONNECT TO
                            else:
                                line=program.Program.all_lines[-1]
                                if obj.id!=line.line_connected_from:
                                    line.connect_to(routerId=obj.id,end_x=mouse[0],end_y=mouse[1])
                                    self.line_first_time=True



    
    def update_event(self,event):
        self.event=event
    def clicked_on_line(self):
        pass    
    def clicked_on_router(self,x,y):
        for obj in program.Program.all_routers:
            if self.selected=='router':
                if obj.pos_x+obj.image.get_size()[0] > x > obj.pos_x-obj.image.get_size()[0]  and obj.pos_y+obj.image.get_size()[1] > y > obj.pos_y-obj.image.get_size()[1]:
                    print('router and clicked on router')
                    return obj
            if self.selected=='line':
                if obj.pos_x+obj.image.get_size()[0] > x > obj.pos_x and obj.pos_y+obj.image.get_size()[1] > y > obj.pos_y:
                    print('line and clicked on router')
                    return obj               
        return None

    
    def create_line(self,start_x,start_y,end_x,end_y):
        line= Line(self.line_color,0,start_x,start_y,end_x,end_y)
        return line

    def create_router(self,pos_x,pos_y):
        router_obj=Router(self.router_image_obj,pos_x,pos_y)
        print(f'ana at3mlt router with id {router_obj.id}')
        return router_obj


    def update(self):
        self.screen.blit(self.background_img, (0,0))
        self.screen.blit(self.draw_img,(100,0))
        self.button(self.router_image_obj,25,50,self.router_image_obj.get_size(),item_type='router')
        self.button(self.draw_img,100,0,self.draw_img.get_size(),item_type='draw')
        self.button(self.line_image_obj,25,150,self.line_image_obj.get_size(),item_type='line')