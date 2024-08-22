import pygame
from pygame.math import Vector2
from asteroid import Asteroid
from circleshape import *
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * float(
            self.radius / 1.5
        )

        a = self.position + (forward * float(self.radius))
        b = self.position - right - (forward * float(self.radius))
        c = self.position + right - (forward * float(self.radius))
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), PLAYER_LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURNING_SPEED * dt

    def move(self, dt):
        self.position += (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_FORWARD_SPEED * dt
        )

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
