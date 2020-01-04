import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate_point(self, angle):
        new_point = Point(self.x * math.cos(angle) - self.y * math.sin(angle),
                          self.y * math.cos(angle) + self.x * math.sin(angle))
        self.x = new_point.x
        self.y = new_point.y
