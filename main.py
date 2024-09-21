import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
import sys
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = [updatable,drawable]
    player = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroids.containers = [asteroids,updatable,drawable]
    AsteroidField.containers = [updatable]
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
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()