class Coordinate (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_sq = (self.x - other.x)**2
        y_sq = (self.y - other.y)**2
        dist = (x_sq + y_sq)**0.5
        return dist
    def getX(self):
        return self.x
    def getY(self):
        return self.y
