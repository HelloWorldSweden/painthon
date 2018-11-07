from tkinter import *
from math import *
from random import *


WIDTH = 500
HEIGHT = 500

class PaintTwicon():
    def __init__(self, **kwargs):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, borderwidth=0, highlightthickness=0, bg="white")
        self.canvas.grid()

    def circle(self, x, y,r, **kwargs):
        return self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.canvas.create_arc(x-r, y-r, x+r, y+r, **kwargs)


    def drawPicture(self, ):
        textX = WIDTH/2
        textY = 10
        self.root.wm_title("Painthon")
        self.root.mainloop()
