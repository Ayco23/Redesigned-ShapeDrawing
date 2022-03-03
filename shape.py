from abc import ABC, abstractmethod
from graphics import Graphics

class Shape(ABC):

    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self, drawmethod: Graphics):
        pass
