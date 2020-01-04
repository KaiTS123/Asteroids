import VectorShapes
from Point import Point
from Vector import Vector
import math
from GameSettings import GameSettings
from PlayerBullet import PlayerBullet


class PlayerShip:
    def __init__(self):
        self.points = [
            Point(0, -15),
            Point(10, 10),
            Point(0, 5),
            Point(-10, 10),
            Point(0, -15)
        ]
        self.position = Vector(GameSettings.screenSize["x"] * 0.5, GameSettings.screenSize["y"] * 0.5)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.rotation = 0
        self.rotationSpeed = 0
        self.bullets = []
        self.time_since_shot = 10

        self.shooting_timeout = 10
        self.rotationAcceleration = 0
        self.thrustStrength = 0.12
        self.turnStrength = 0.005
        self.decelerationAmount = 0.02
        self.decelerationAmountTurning = 0.1

    def draw(self, screen):
        VectorShapes.drawShape(screen, self, (255, 255, 255))
        self.drawBullets(screen)

    def update(self):
        self.velocity.add(self.acceleration)
        self.rotationSpeed += self.rotationAcceleration

        self.position.add(self.velocity)
        self.rotation += self.rotationSpeed

        self.acceleration.x = -self.velocity.x * self.decelerationAmount
        self.acceleration.y = -self.velocity.y * self.decelerationAmount
        self.rotationAcceleration = -self.rotationSpeed * self.decelerationAmountTurning

        self.updateBullets()
        self.time_since_shot += 1

        self.position.wraparound(GameSettings.screenSize["x"], GameSettings.screenSize["y"])

    def rotateRight(self):
        self.rotationAcceleration = self.turnStrength

    def rotateLeft(self):
        self.rotationAcceleration = -self.turnStrength

    def thrustForward(self):
        self.acceleration.x = self.thrustStrength * math.sin(self.rotation)
        self.acceleration.y = self.thrustStrength * -math.cos(self.rotation)

    def reset(self):
        self.position = Vector(GameSettings.screenSize["x"] * 0.5, GameSettings.screenSize["y"] * 0.5)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.rotation = 0
        self.rotationSpeed = 0
        self.bullets = []

    def shootBullet(self):
        if self.time_since_shot > self.shooting_timeout:
            bullet = PlayerBullet(self.position, self.rotation, self.velocity)
            self.bullets.append(bullet)
            self.time_since_shot = 0

    def updateBullets(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.life >= PlayerBullet.lifespan:
                self.bullets.remove(bullet)

    def drawBullets(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
