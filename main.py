import pygame

width=400
height=300
pygame.init()
screen = pygame.display.set_mode((width,height))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()