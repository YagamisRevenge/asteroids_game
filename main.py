import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = [updatable,drawable]
    Shot.containers = [shots,drawable,updatable]
    Asteroids.containers = [asteroids,updatable,drawable]
    AsteroidField.containers = [updatable]
    player = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        for i in updatable:
            i.update(dt)
        for i in asteroids:
            if i.collision(player):
                print("Game over!")
                sys.exit()
        for i in drawable:
            i.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
                    asteroid.split()
                    

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()