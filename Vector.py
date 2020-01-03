class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def wraparound(self, max_x, max_y):
        if self.x > max_x:
            self.x = 0
        if self.x < 0:
            self.x = max_x
        if self.y > max_y:
            self.y = 0
        if self.y < 0:
            self.y = max_y
