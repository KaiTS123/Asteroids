# external libraries
import copy
import math
import random
from typing import List

# internal libraries
import VectorShapes
from Point import Point
from Vector import Vector
from GameSettings import GameSettings


class Asteroid:
    min_initial_velocity = 0.5
    max_initial_velocity = 2
    max_initial_rotation = 0.05
    initial_radius = 40
    radius_variation_positive = 10
    radius_variation_negative = -25
    shape_num_points = 9
    color = (255, 255, 255)

    velocity: Vector
    position: Vector

    def __init__(self):
        # setup shape
        self.points = [Point(self.initial_radius, 0)]
        for point in range(1, self.shape_num_points - 1):
            angle = (math.pi * 2) * point / self.shape_num_points
            radius = self.initial_radius + random.randint(self.radius_variation_negative,
                                                          self.radius_variation_positive)
            self.points.append(Point(radius * math.cos(angle), radius * math.sin(angle)))
        self.points.append(Point(self.initial_radius, 0))

        # setup initial position and rotation
        if random.randint(0, 1) == 0:
            self.position = Vector(random.randint(0, GameSettings.screenSize["x"]), 0)
        else:
            self.position = Vector(0, random.randint(0, GameSettings.screenSize["y"]))

        self.rotation = 0.0
        velocity_angle = random.uniform(0, math.pi * 2)
        velocity_speed = random.uniform(self.min_initial_velocity, self.max_initial_velocity)
        self.velocity = Vector(velocity_speed * math.sin(velocity_angle), velocity_speed * math.cos(velocity_angle))
        self.rotation_speed = random.uniform(-self.max_initial_rotation, self.max_initial_rotation)

    def rotate(self):
        self.rotation += self.rotation_speed
        if self.rotation >= (math.pi * 2):
            self.rotation -= (math.pi * 2)
        elif self.rotation < 0:
            self.rotation += (math.pi * 2)

    def move(self):
        self.position.add(self.velocity)
        self.position.wraparound(GameSettings.screenSize["x"], GameSettings.screenSize["y"])
        self.rotate()

    def draw(self, screen):
        VectorShapes.drawShape(screen, self, self.color)
