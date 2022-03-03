from shape import Shape
import math
from graphics import Graphics

class Triangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, color: str):
        super().__init__(x, y, color)
        self.width: int = width
        self.height: int = height

    def draw(self, drawmethod: Graphics):
        pts = self.get_pts()
        drawmethod.draw_squared_shape(pts, self.color)

    def get_pts(self):
        pts = []
        pts.append(self.x + self.width/2)
        pts.append(self.y)
        pts.append(self.x + self.width)
        pts.append(self.y+ self.height)
        pts.append(self.x)
        pts.append(self.y+ self.height)
        pts.append(self.x + self.width/2)
        pts.append(self.y)
        return pts
