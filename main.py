import pygame
from program import Program


WIDTH=1024
HEIGHT=768
GREY=(210, 210 ,210)
FPS=30
BACKGROUND_COLOR=GREY     #GREY
TITLE='ROUTING NETWORK SOFTWARE'


    
def main():
        #window information
        pygame.init()
        pygame.display.set_caption(TITLE)
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        done = False
        clock=pygame.time.Clock()
        #creating main sprites
        my_program=Program(screen=screen,bkcolor=GREY)
        #starting the game loop
        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                # paint to screen        
         #       screen.fill(BACKGROUND_COLOR)
                my_program.update()
                pygame.display.flip()
                #set the FPS
                clock.tick(FPS)

#routing
if __name__ == "__main__":
    main()