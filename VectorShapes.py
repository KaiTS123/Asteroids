import copy
import pygame
import math

from Point import Point
from Line import Line
from Vector import Vector


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


def shapesColliding(shape1, shape2):
    for point in shape1.points:
        rotatedPoint = Point(
            point.x * math.cos(shape1.rotation) - point.y * math.sin(shape1.rotation),
            point.y * math.cos(shape1.rotation) + point.x * math.sin(shape1.rotation)
        )
        rotatedPoint.x += shape1.position.x
        rotatedPoint.y += shape1.position.y
        if pointWithinShape(rotatedPoint, shape2):
            return True
    return False


def pointWithinShape(point, shape):
    isFirstPoint = True
    angle = shape.rotation
    num_intersections_left = 0
    num_intersections_right = 0
    for point2 in shape.points:
        rotatedPoint = Point(
            point2.x * math.cos(angle) - point2.y * math.sin(angle) + shape.position.x,
            point2.y * math.cos(angle) + point2.x * math.sin(angle) + shape.position.y
        )
        if isFirstPoint:
            lastPoint = copy.deepcopy(rotatedPoint)
            isFirstPoint = False
        else:
            line = Line(rotatedPoint, lastPoint)
            if line.check_intercept(point) == 1:
                num_intersections_left += 1
            if line.check_intercept(point) == 2:
                num_intersections_right += 1
            lastPoint = copy.deepcopy(rotatedPoint)
    if num_intersections_left % 2 == 1 and num_intersections_right % 2 == 1:
        return True
    else:
        return False
