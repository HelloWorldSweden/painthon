from tkinter import *
from math import *
from random import *


WIDTH = 500
HEIGHT = 500

class PaintCanvas():
    def __init__(self, circleArea, rectangleArea):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, borderwidth=0, highlightthickness=0, bg="white")
        self.canvas.grid()

        self.cirleArea = circleArea
        self.rectangleArea = rectangleArea
        self.totalArea = 0

    def circle(self, x, y,r, **kwargs):
        self.totalArea += self.cirleArea(r)
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    
    def dynamic_rectangle(self, x1, y1, x2, y2, **kwargs):
        return self.canvas.create_line(x1, y1, x2, y2, **kwargs)

    def shapy(self, array, **kwargs):
        return self.canvas.create_polygon(array, **kwargs)

    def circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.canvas.create_arc(x-r, y-r, x+r, y+r, **kwargs)

    def rectangle(self, x1, y1, x2, y2, **kwargs):
        self.totalArea += self.rectangleArea(x1, y1, x2, y2)
        return self.canvas.create_rectangle(x1, y1, x2, y2, **kwargs)


    def drawPicture(self, ):
        textX = WIDTH/2
        textY = 10
        self.canvas.create_text(textX, textY, text="Total area ≈ {} p²".format(self.totalArea),
                                font="helvetica")
        self.root.wm_title("Painthon")
        self.root.mainloop()
