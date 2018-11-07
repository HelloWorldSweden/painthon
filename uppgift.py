from HelloLibrary.AreaPainter import *


#------------- Skriv dina egna funktioner här
def circle_area(r):
    return 100

def rectangle_area(x1, x2, y1, y2):
    return 100

paint = PaintCanvas(circle_area, rectangle_area)
#-------------------------------------------


#Skapa en cirkel igenom att använda funktionen:
#   paint.circle(x-positon, y-positon, radie)
radie = 50
x = 100
y = 100
paint.circle(x, y, radie, fill="")

#Skapa en rektangel igenom att använda funktionen:
#   paint.rectangle(x1-positon, y1-positon, x2-positon, y2-positon,)
x1 = 200
y1 = 200
x2 = 300
y2 = 300
paint.rectangle(x1, y1, x2, y2, fill="")


#----------------- Här ritar vi upp bilden
paint.drawPicture()
