import json
from circle import Circle
from rectangle import Rectangle
from star import Star
from triangle import Triangle
from shape import Shape
from typing import List

class Parser:

    def parse_shapes(self, filename: str) -> List[Shape]:
        json_file = open(filename)
        data = json.load(json_file)
        shapes: List[Shape] = []
        for shape_def in data:
            if shape_def["type"] == "circle":
                shapes.append(Circle(shape_def["x"], shape_def["y"], shape_def["radius"], shape_def["color"]))
            elif shape_def["type"] == "rectangle":
                shapes.append(Rectangle(shape_def["x"], shape_def["y"], shape_def["width"], shape_def["height"], shape_def["color"]))
            elif shape_def["type"] == "star":
                shapes.append(Star(shape_def["x"], shape_def["y"], shape_def["width"], shape_def["height"], shape_def["color"]))
            elif shape_def["type"] == "triangle":
                shapes.append(Triangle(shape_def["x"], shape_def["y"], shape_def["width"], shape_def["height"], shape_def["color"]))
        return shapes
