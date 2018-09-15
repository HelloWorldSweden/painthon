from HelloLibrary.AreaPainter import *

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

paint.drawPicture()
