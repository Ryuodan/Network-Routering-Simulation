import pygame
from router import Router
from line import Line
import program


class ItemFactory:
    def __init__(self,screen,shelf_color,shelf_width,shelf_height,draw_width,
                draw_height,draw_color,router_img,line_img,line_color):
        #INTIAL VALUES
        self.screen=screen
        self.event=None
        self.selected=None
        self.line_first_time=True
        self.line_color=line_color
        self.marked_color=(0,0,255) #BLUE
        #LOAD IMAGES
        self.router_image_obj = pygame.image.load(router_img)
        self.line_image_obj = pygame.image.load(line_img)

        #SET BACKGROUND 
        self.background_img = pygame.Surface([shelf_width, shelf_height])
        pygame.draw.rect(self.background_img , shelf_color, [0, 0, shelf_width, shelf_height]) 

        #DRAW AREA 
        self.draw_img = pygame.Surface([draw_width, draw_height])
        pygame.draw.rect(self.draw_img , draw_color, [0, 0, draw_width, draw_height]) 


    def button(self,img,pos_x,pos_y,size,item_type):
        def mark_button(x1,y1,x2,y2):
            thickness=3
            pygame.draw.rect(self.screen,self.marked_color,
                            (x1,y1,x2,y2),thickness)
        #DRAW BUTTON IMG
        self.screen.blit(img,(pos_x,pos_y))
        width,height=size
        #DRAW SELECTED BORDER
        if self.selected=='router' and item_type=='router':
            mark_button(pos_x,pos_y,width,height)

        elif self.selected=='line' and item_type=='line':
            mark_button(pos_x,pos_y,width,height)

        #GET MOUSE POSITION
        mouse = pygame.mouse.get_pos()        
        #HANDLE ACTIONS
        if pos_x+width > mouse[0] > pos_x and pos_y+height > mouse[1] > pos_y:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            #when right clicked unselect all
            if self.event.type ==pygame.MOUSEBUTTONDOWN and self.event.button==3:
                #RESET everything
                self.selected=None
                self.line_first_time=True

            #when left clicked select and do all functioanlity
            if self.event.type == pygame.MOUSEBUTTONDOWN and self.event.button == 1: #action != None:

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
                        #IF IT'S INSIDE A ROUTER
                        if obj is not None:
                            #GET MIDDLE OF THE ROUTER
                            middle_of_router_img_x=obj.pos_x+obj.image.get_size()[0]/2
                            middle_of_router_img_y=obj.pos_y+obj.image.get_size()[1]/2

                            #CONNECT FROM
                            if self.line_first_time:
                                line=self.create_line(0,0,0,0)###you stoped here connect lines to routers 
                                line.connect_from(
                                            routerId=obj.id,
                                            pos_x=middle_of_router_img_x,
                                            pos_y=middle_of_router_img_y)
                                program.Program.all_lines.append(line)
                                self.line_first_time=False

                            #CONNECT TO
                            else:
                                line=program.Program.all_lines[-1]
                                if obj.id!=line.routerId_from:
                                    line.connect_to(
                                            routerId=obj.id,
                                            pos_x=middle_of_router_img_x,
                                            pos_y=middle_of_router_img_y)
                                    self.line_first_time=True
                                    self.selected=None
                                    print(f'ana at3mlt line been router {line.routerId_from} ---> router {line.routerId_to}')
      



    
    def update_event(self,event):
        self.event=event


    def clicked_on_router(self,x,y):
        for obj in program.Program.all_routers:
            if self.selected=='router':
                if obj.pos_x+obj.image.get_size()[0] > x > obj.pos_x-obj.image.get_size()[0]  and obj.pos_y+obj.image.get_size()[1] > y > obj.pos_y-obj.image.get_size()[1]:
#                    print('router and clicked on router')
                    return obj
            if self.selected=='line':
                if obj.pos_x+obj.image.get_size()[0] > x > obj.pos_x and obj.pos_y+obj.image.get_size()[1] > y > obj.pos_y:
 #                   print('line and clicked on router')
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