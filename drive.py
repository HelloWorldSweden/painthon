from tkinter import *
from math import *
from func import *
from uppgift import *

root = Tk()
canvas = Canvas(root, width=500, height=500, borderwidth=0, highlightthickness=0, bg="white")
canvas.pack()



id = canvas.create_text(250, 470, text="Cirkelns area ≈ " + str(round(circle_area(r), 2)) + " p²", font="helvetica")
id = canvas.create_text(250, 490, text="Rektangelns area = " + str(rectangle_area(x1, x2, y1, y2)) + " p²", font="helvetica")
id = canvas.create_text(250, 450, text="Totala arean ≈ " + str(round(rectangle_area(x1, x2, y1, y2) + circle_area(r), 2)) + " p²", font="helvetica")


root.wm_title("Matteverkstan")
root.mainloop()
