from shape import Shape
from graphics import Graphics

class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int, color: str):
        super().__init__(x, y, color)
        self.radius: int = radius
        
    def draw(self, drawmethod: Graphics):
        pts = self.get_pts()
        drawmethod.draw_rounded_shape(pts, self.color)

    def get_pts(self) -> list:
        pts = []
        pts.append(self.x - self.radius)
        pts.append(self.y - self.radius)
        pts.append(self.x + self.radius)
        pts.append(self.y + self.radius)
        return pts
