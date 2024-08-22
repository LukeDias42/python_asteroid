import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH
        )

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        rotation = random.uniform(20, 50)
        Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        ).velocity = self.velocity.rotate(rotation) * ASTEROID_SPEED_INCREASE
        Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        ).velocity = self.velocity.rotate(-rotation) * ASTEROID_SPEED_INCREASE

    def update(self, dt):
        self.move(dt)