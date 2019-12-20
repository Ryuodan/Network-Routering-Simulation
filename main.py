import pygame
from router import Router
from spriteFactory import SpriteFactory
WIDTH=1024
HEIGHT=768
BLACK=(0,0,0)
GREY=(210, 210 ,210)
BACKGROUND_COLOR=GREY     #GREY
TITLE='ROUTING NETWORK SOFTWARE'


    
def main():
        #window information
        pygame.init()
        pygame.display.set_caption(TITLE)
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        done = False
        all_sprites_list = pygame.sprite.Group()
        
        #creating main sprites

       # router_1=Router(10,10)
        clock=pygame.time.Clock()
        sprite_factory=SpriteFactory(screen,BLACK,100,HEIGHT)
         # paint to screen
       # all_sprites_list.add(sprite_factory)
      #  all_sprites_list.add(router_1)
        #starting the game loop
        while not done:
                all_sprites_list.update()

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True

                screen.fill(BACKGROUND_COLOR)
                sprite_factory.update()
             #   all_sprites_list.draw(screen)
                pygame.display.flip()
                clock.tick(60)

#routing
if __name__ == "__main__":
    main()