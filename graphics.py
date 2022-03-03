from abc import ABC, abstractmethod
from tkinter import Canvas
import svgwrite
import pylatex

class Graphics(ABC):

    @abstractmethod
    def draw_squared_shape(self, pts: list):
        pass

    @abstractmethod
    def draw_rounded_shape(self, pts: list):
        pass

class PythonGraphics(Graphics):

    def __init__(self):
        self.drawlocation: Canvas

    def draw_squared_shape(self, pts: list, color: str):
        self.drawlocation.create_polygon(*pts, outline="black", fill=color, width=2)

    def draw_rounded_shape(self, pts: list, color: str):
        self.drawlocation.create_oval(*pts, fill=color, width=2)

class SVGGraphics(Graphics):

    def __init__(self):
        self.drawlocation: svgwrite.Drawing
    
    def draw_squared_shape(self, pts: list, color: str):
        #create a pair of points for every x and y value in pts
        p = []
        i = 0
        while i < len(pts):
            x = (pts[i], pts[i+1])
            p.append(x)
            i += 2
        
        self.drawlocation.add(svgwrite.shapes.Polyline(points=p, stroke_width = "2", stroke = "black", fill = color))

    def draw_rounded_shape(self, pts: list, color: str):
        # calculate x, y and radius from the given points
        x = (pts[0]+pts[2])/2
        y = (pts[1]+pts[3])/2
        radius = pts[2] - x
        self.drawlocation.add(svgwrite.shapes.Circle(center=(x, y), r=radius, stroke_width = "2", stroke = "black", fill = color))

from pylatex import (Document, TikZ, TikZDraw, TikZCoordinate, TikZOptions)     

class LatexGraphics(Graphics):

    def __init__(self):
        self.drawlocation: Document

    def draw_squared_shape(self, pts: list, color: str):
        #TO DO
        print("Add squared shape to LateX Document")
        #create a pair of points for every x and y value in pts
        i = 0
        while i < len(pts):
            self.drawlocation.create(TikZ()).append(TikZDraw([TikZCoordinate(pts[i], pts[i+1]),'rectangle', TikZCoordinate(pts[i+2], pts[i+4])], options=TikZOptions(fill='red')))
            i += 4


    def draw_rounded_shape(self, pts: list):
        #TO DO
        print("Add round shape to LateX Document")
