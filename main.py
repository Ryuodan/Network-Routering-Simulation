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

        router_1=Router(10,10)
        
        sprite_factory=SpriteFactory(BLACK,100,HEIGHT)
        
        all_sprites_list.add(sprite_factory)
        all_sprites_list.add(router_1)
        #starting the game loop
        while not done:
                all_sprites_list.update()

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True

                screen.fill(BACKGROUND_COLOR)
                all_sprites_list.draw(screen)
                pygame.display.flip()


#routing
if __name__ == "__main__":
    main()