import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        Asteroid.containers = (updatable, drawable, asteroids)
        Player.containers = (updatable, drawable)
        AsteroidField.containers = updatable
        Shot.containers = (shots, updatable, drawable)

        asteroids_field = AsteroidField()
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            for object in updatable:
                object.update(dt)

            for object in asteroids:
                if object.is_colliding(player):
                    print("Game over!")
                    raise SystemExit
                
                for bullet in shots:
                    if object.is_colliding(bullet):
                        bullet.kill()
                        object.split()
            


            screen.fill(pygame.Color(0,0,0,255))
            
            for object in drawable:
                object.draw(screen)

            pygame.display.flip()
            
            dt = clock.tick(60.0)/1000.0 # from milliseconds to seconds

if __name__ == "__main__":
    main()