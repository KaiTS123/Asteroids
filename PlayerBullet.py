from Vector import Vector
from Point import Point
import math
import pygame
from GameSettings import GameSettings


class PlayerBullet:
    bullet_speed = 6
    radius = 1
    lifespan = 300  # in frames

    def __init__(self, position, direction, player_velocity):
        self.position = Vector(position.x, position.y)
        self.velocity = Vector(player_velocity.x + self.bullet_speed * math.sin(direction),
                               player_velocity.y - self.bullet_speed * math.cos(direction))
        self.life = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           (math.floor(self.position.x), math.floor(self.position.y)), self.radius)

    def move(self):
        self.position.add(self.velocity)
        self.position.wraparound(GameSettings.screenSize["x"], GameSettings.screenSize["y"])
        self.life += 1
