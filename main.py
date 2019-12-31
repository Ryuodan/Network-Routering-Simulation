import pygame
from program import Program


WIDTH=1024
HEIGHT=768
GREY=(210, 210 ,210)
FPS=60
BACKGROUND_COLOR=GREY     #GREY
TITLE='ROUTING NETWORK SOFTWARE'
pygame.init()

def main():
        #window information
        font = pygame.font.Font(None, 32) 
        pygame.display.set_caption(TITLE)
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        done = False
        clock=pygame.time.Clock()
        #creating main sprites
        my_program=Program(screen=screen,bkcolor=GREY,font=font)
        #starting the game loop
        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                        my_program.update_event(event)
                # paint to screen        
         #       screen.fill(BACKGROUND_COLOR)
                my_program.update()
                pygame.display.flip()
                #set the FPS
                clock.tick(FPS)

#routing
if __name__ == "__main__":
    main()