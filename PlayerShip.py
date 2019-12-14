import vectors
from Point import Point
from Vector import Vector
import math


class PlayerShip:
    def __init__(self):
        self.points = [
            Point(0, -15),
            Point(10, 10),
            Point(0, 5),
            Point(-10, 10),
            Point(0, -15)
        ]
        self.position = Vector(250, 250)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.rotation = 0
        self.rotationSpeed = 0
        self.rotationAcceleration = 0
        self.thrustStrength = 0.12
        self.turnStrength = 0.005
        self.decelerationAmount = 0.02
        self.decelerationAmountTurning = 0.1

    def draw(self, screen):
        vectors.drawShape(screen, self, (100, 100, 255))

    def update(self):
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.rotationSpeed += self.rotationAcceleration

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.rotation += self.rotationSpeed

        self.acceleration.x = -self.velocity.x * self.decelerationAmount
        self.acceleration.y = -self.velocity.y * self.decelerationAmount
        self.rotationAcceleration = -self.rotationSpeed * self.decelerationAmountTurning

        if self.position.x > 510: self.position.x = -10
        if self.position.x < -10: self.position.x = 510
        if self.position.y > 510: self.position.y = -10
        if self.position.y < -10: self.position.y = 510

    def rotateRight(self):
        self.rotationAcceleration = self.turnStrength

    def rotateLeft(self):
        self.rotationAcceleration = -self.turnStrength

    def thrustForward(self):
        self.acceleration.x = self.thrustStrength * math.sin(self.rotation)
        self.acceleration.y = self.thrustStrength * -math.cos(self.rotation)
