from Point import Point
import copy


class Line:
    point1: Point
    point2: Point

    def __init__(self, point1, point2):
        self.point1 = copy.deepcopy(point1)
        self.point2 = copy.deepcopy(point2)

    def check_intercept(self, point):
        # 1 is left, 2 is right, 0 is no intercept
        if ((self.point1.y > point.y) and (self.point2.y <= point.y)) or (
                (self.point1.y <= point.y) and (self.point2.y > point.y)):
            if self.point2.x == self.point1.x:
                if self.point2.x <= point.x:
                    return 1
                else:
                    return 2
            else:
                if (self.point1.x <= point.x) and (self.point2.x <= point.x):
                    return 1
                if (self.point1.x >= point.x) and (self.point2.x >= point.x):
                    return 2
                else:
                    gradient = (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
                    intercept_x = ((point.y - self.point1.y) / gradient) + self.point1.x
                    if intercept_x <= point.x:
                        return 1
                    else:
                        return 2
        else:
            return 0
