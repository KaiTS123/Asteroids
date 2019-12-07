import pygame
import math


def drawShape(screen, shape):
    isFirstPoint = True
    angle = shape["rotation"]
    for point in shape["points"]:
        rotatedPoint = {
            "x": point["x"] * math.cos(angle) - point["y"] * math.sin(angle),
            "y": point["y"] * math.cos(angle) + point["x"] * math.sin(angle)
        }
        if isFirstPoint:
            lastPoint = rotatedPoint
            isFirstPoint = False
        else:
            pygame.draw.line(screen, (255, 255, 255),
                             (lastPoint["x"] + shape["position"]["x"], lastPoint["y"] + shape["position"]["y"]),
                             (rotatedPoint["x"] + shape["position"]["x"], rotatedPoint["y"] + shape["position"]["y"]),
                             1)
            lastPoint = rotatedPoint
