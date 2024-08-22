import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = updatables
    Shot.containers = (updatables, drawables, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        dt = game_clock.tick(FPS) / 1000
        for game_object in updatables:
            game_object.update(dt)
        for game_object in drawables:
            game_object.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()


if __name__ == "__main__":
    main()
