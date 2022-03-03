from shape import Shape
from graphics import Graphics

class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, color: str):
        super(Rectangle,self).__init__(x,y,color)
        self.width: int = width
        self.height: int = height

    def draw(self, drawmethod: Graphics):
        pts = self.get_pts()
        #Draw the shape using the pts
        drawmethod.draw_squared_shape(pts, self.color)

    def get_pts(self) -> list:
        #Append all points to a list
        pts = []
        pts.append(self.x)
        pts.append(self.y)
        pts.append(self.x + self.width)
        pts.append(self.y)
        pts.append(self.x + self.width)
        pts.append(self.y + self.height)
        pts.append(self.x)
        pts.append(self.y + self.height)
        pts.append(self.x)
        pts.append(self.y)
        return pts
