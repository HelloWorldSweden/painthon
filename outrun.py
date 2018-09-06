from tkinter import *
from math import *
from random import *

root = Tk()
canvas = Canvas(root, width=500, height=500, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()

#--------------------------- Magiska funktioner -----------------------------

def _create_circle(self, x, y,r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle_arc = _create_circle_arc

#---------------------------- Skriv täckningen nedan -----------------------
f = 275

hl = 300


canvas.create_line(0, hl, 500, hl, fill="cyan")
# Center
canvas.create_line(250, f, 250, 500, fill="cyan")

# Left

canvas.create_line(250, f, 125, 500, fill="cyan")

canvas.create_line(250, f, 0, 480, fill="cyan")

canvas.create_line(250, f, 0, 400, fill="cyan")

canvas.create_line(250, f, 0, 350, fill="cyan")

canvas.create_line(250, f, 0, 320, fill="cyan")

# Right

canvas.create_line(250, f, 375, 500, fill="cyan")

canvas.create_line(250, f, 500, 480, fill="cyan")

canvas.create_line(250, f, 500, 400, fill="cyan")

canvas.create_line(250, f, 500, 350, fill="cyan")

canvas.create_line(250, f, 500, 320, fill="cyan")

canvas.create_rectangle(0, 0, 500, hl-1, fill="black")

# Horizontal lines
i = 300
x = 2

while (i<600):
    canvas.create_line(0, i, 500, i, fill="cyan")
    i = i + x
    x = pow(x, 1.2)

# stars

s = 1
while (s<150):
    x = randint(0, 498)
    y = randint(0, 298)
    canvas.create_rectangle(x, y, x+randint(1,3), y+randint(1,3), fill="white")
    s = s+1

# sun

canvas.create_circle_arc(250, 250, 100, fill="orange", start=0, end=180)

canvas.create_rectangle(151, 255, 349, 260, fill="#ff6666")

canvas.create_rectangle(152, 265, 348, 270, fill="#ff6699")

canvas.create_rectangle(155, 275, 345, 280, fill="#ff3399")

canvas.create_rectangle(161, 285, 339, 290, fill="#ff33cc")

canvas.create_rectangle(169, 295, 331, 299, fill="#cc0099")


#canvas.create_circle_arc(250, 250, 100, style="arc", outline="#ff6666", start=185, end=190)
#canvas.create_circle_arc(250, 250, 100, style="arc", outline="#ff6666", start=350, end=355)

#canvas.create_line(152, 259, 348, 259, fill="#ff6666")


root.wm_title("Outrun")
root.mainloop()
