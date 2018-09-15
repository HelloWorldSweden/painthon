from tkinter import *
from math import *
from random import *


WIDTH = 500
HEIGHT = 500

class PaintSunset():
    def __init__(self, **kwargs):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, borderwidth=0, highlightthickness=0, bg="black")
        self.canvas.grid()

    def circle(self, x, y,r, **kwargs):
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.canvas.create_arc(x-r, y-r, x+r, y+r, **kwargs)



    def line(self, x1, y1, x2, y2, **kwargs):
        return self.canvas.create_line(x1, y1, x2, y2, **kwargs)

    def rectangle(self, x1, y1, x2, y2, **kwargs):
        return self.canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

    def drawPicture(self, ):
        textX = WIDTH/2
        textY = 10
        self.root.wm_title("Painthon")
        self.root.mainloop()
