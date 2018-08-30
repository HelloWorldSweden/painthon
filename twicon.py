from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500, borderwidth=0, highlightthickness=0, bg="white")
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

#--------------------------- Jobba med dessa ---------------------------------

gr = 1.618034

r = 40


# first big blue
canvas.create_circle_arc(r*5, r*5, r*gr*2, fill="blue", outline="black", start=200, end=360)

canvas.create_circle(r*4.5, r*4, r, fill="blue", outline="black")

# wings
canvas.create_circle(r*3.5, r*6, r*gr, fill="white", outline="black")

canvas.create_circle(r*4.75, r*5.5, r*gr, fill="blue", outline="black")
canvas.create_circle(r*3.75, r*5, r*gr, fill="white", outline="black")

canvas.create_circle(r*4.75, r*5, r*gr, fill="blue", outline="black")
canvas.create_circle(r*3.75, r*4.25, r*gr, fill="white", outline="black")

canvas.create_circle(r*5, r*4.5, r*gr, fill="blue", outline="black")

# big top white
canvas.create_circle(r*6, r*2.25, r*gr*2, fill="white", outline="black")

# beaks

canvas.create_circle_arc(r*7.75, r*4.75, r, fill="blue", outline="black", start=200, end=360)
canvas.create_circle(r*8.15, r*4.25, r, fill="white", outline="black")

canvas.create_circle_arc(r*7.5, r*4.35, r, fill="blue", outline="black", start=200, end=360)
canvas.create_circle(r*7.85, r*3.75, r, fill="white", outline="black")


# head
canvas.create_circle(r*7, r*5.25, r, fill="blue", outline="black")


#-------------------------------------------------------------------------------

root.wm_title("Twicon")
root.mainloop()
