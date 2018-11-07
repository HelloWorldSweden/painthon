from HelloLibrary.AreaPainter import *

#------------- Skriv dina egna funktioner här
def circle_area(r):
    return 100

def rectangle_area(x1, x2, y1, y2):
    return 100

paint = PaintCanvas(circle_area, rectangle_area)
#-------------------------------------------


#paint.rektangel(x1, y1, x2, y2,)
x1 = 200
y1 = 300
x2 = 300
y2 = 400
paint.rectangle(x1, y1, x2, y2, fill="green")
paint.rectangle(100, 200, 200, 300, fill="red")
paint.dynamic_rectangle(200, 200, 300, 300, fill="black") 
arr = [200, 200, 300, 300, 400, 200, 300, 100]
paint.shapy(arr, fill="blue")

paint.drawPicture()
