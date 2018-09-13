from tkinter import *
from math import *
#from drive import *



#--------------------------- Magiska funktioner -----------------------------

def cirkel(x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs, fill="blue")

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.circle_arc = _create_circle_arc


def rektangel(x1, y1, x2, y2):
    return canvas.create_rectangle(x1, y1, x2, y2)



#------------------------------------------------------------------------
