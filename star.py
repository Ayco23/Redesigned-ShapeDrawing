from shape import Shape
import math
from graphics import Graphics

class Star(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, color: str):
        super().__init__(x, y, color)
        self.width: int = width
        self.height: int = height

    def draw(self, drawmethod: Graphics):
        pts = self.get_pts()
        drawmethod.draw_squared_shape(pts, self.color)

    def get_pts(self):
        numPoints = 5
        pts = []
        rx = self.width / 2
        ry = self.height / 2
        cx = self.x + rx
        cy = self.y + ry
        theta = -math.pi / 2
        dtheta = 4 * math.pi / numPoints

        for i in range(0, numPoints + 1):
            pts.append(int(round(cx + rx * math.cos(theta))))
            pts.append(int(round(cy + ry * math.sin(theta))))
            theta += dtheta
            
        return pts
