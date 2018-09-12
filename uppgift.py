from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid()


#--------------------------- Magiska funktioner -----------------------------

def cirkel(x, y,r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)


def cirkel_del(x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return canvas.create_arc(x-r, y-r, x+r, y+r, **kwargs)

def rektangel(x1, y1, x2, y2):
    return canvas.create_rectangle(x1, y1, x2, y2)


#--------------------------- Jobba här ---------------------------------
# Skapa en variabel r, för radius


# Fyll i koordinaterna x och y, samt radius för att skapa en cirkel. Välj även färg
cirkel( x, y, r, fill="")

#Fyll i koordinaterna x1, x2 och y1, y2. Välj även en färg.

rektangel(x1, y1, x2, y2, fill="")

def cirkel_area(radius):
    return pi*radius*radius

#------------------------------------------------------------------------
root.wm_title("Outrun")
root.mainloop()
