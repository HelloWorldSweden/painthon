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

#--------------------------- Jobba här ---------------------------------
# Skapa en variabel r, för radius


# Fyll i koordinaterna x och y, samt radius för att skapa en cirkel. Välj även färg
canvas.create_circle( , , , fill="")

#Fyll i koordinaterna x1, x2 och y1, y2. Välj även en färg.

canvas.create_rectangle(, , , , fill="")

def circle_area(self, r):
    return

#------------------------------------------------------------------------
root.wm_title("Outrun")
root.mainloop()
