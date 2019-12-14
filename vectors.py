import copy
import pygame
import math

from Point import Point


def drawShape(screen, shape, color):
    isFirstPoint = True
    angle = shape.rotation
    for point in shape.points:
        rotatedPoint = Point(
            point.x * math.cos(angle) - point.y * math.sin(angle),
            point.y * math.cos(angle) + point.x * math.sin(angle)
        )
        if isFirstPoint:
            lastPoint = copy.deepcopy(rotatedPoint)
            isFirstPoint = False
        else:
            pygame.draw.line(screen, color,
                             (lastPoint.x + shape.position.x, lastPoint.y + shape.position.y),
                             (rotatedPoint.x + shape.position.x, rotatedPoint.y + shape.position.y),
                             1)
            lastPoint = copy.deepcopy(rotatedPoint)
