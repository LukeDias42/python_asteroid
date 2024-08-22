import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_LINE_WIDTH)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)