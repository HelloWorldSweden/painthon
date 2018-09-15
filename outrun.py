from HelloLibrary.SunsetPainter import *
paint = PaintSunset()

# Vertikal linjer

f = 275
hl = 300

paint.line(0, hl, 500, hl, fill="cyan")

# Center

paint.line(250, f, 250, 500, fill="cyan")

# Left

paint.line(250, f, 125, 500, fill="cyan")

paint.line(250, f, 0, 480, fill="cyan")

paint.line(250, f, 0, 400, fill="cyan")

paint.line(250, f, 0, 350, fill="cyan")

paint.line(250, f, 0, 320, fill="cyan")

# Right

paint.line(250, f, 375, 500, fill="cyan")

paint.line(250, f, 500, 480, fill="cyan")

paint.line(250, f, 500, 400, fill="cyan")

paint.line(250, f, 500, 350, fill="cyan")

paint.line(250, f, 500, 320, fill="cyan")

paint.rectangle(0, 0, 500, hl-1, fill="black")

# Horisontella linjer
i = 300
x = 2

while (i<600):
    paint.line(0, i, 500, i, fill="cyan")
    i = i + x
    x = pow(x, 1.2)

# Stjärnor

s = 1
while (s<150):
    x = randint(0, 498)
    y = randint(0, 298)
    paint.rectangle(x, y, x+randint(1,3), y+randint(1,3), fill="white")
    s = s+1

# Solen

paint.circle_arc(250, 250, 100, fill="orange", start=0, end=180)

paint.rectangle(151, 255, 349, 260, fill="#ff6666")

paint.rectangle(152, 265, 348, 270, fill="#ff6699")

paint.rectangle(155, 275, 345, 280, fill="#ff3399")

paint.rectangle(161, 285, 339, 290, fill="#ff33cc")

paint.rectangle(169, 295, 331, 299, fill="#cc0099")

#----------------- Här ritar vi upp bilden
paint.drawPicture()
