import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    if pygame.get_init():

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        clock = pygame.time.Clock()
        dt = 0.0

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()

        Player.containers = (updatable, drawable)

        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            for object in updatable:
                object.update(dt)

            screen.fill(pygame.Color(0,0,0,255))
            
            for object in drawable:
                object.draw(screen)

            pygame.display.flip()
            
            dt = clock.tick(60.0)/1000.0 # from milliseconds to seconds

if __name__ == "__main__":
    main()