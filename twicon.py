from HelloLibrary.TwiconPainter import *
paint = PaintTwicon()

# r står för radien som är 40.
r = 40

# gs står för gyllene snittet och har värdet 1.618034
# När vi vill ha en större cirkel multiplicerar vi radien med gyllene snittet

gs = 1.618034

kontur = ""

#---------------------- Uppgiften ------------------------

# STORA BLÅ CIRKELN

paint.circle_arc(r*5, r*5, r*gs*2, fill="blue", outline=kontur, start=200, end=360)


# Fyll i x = 180
# Fyll i y = 160

#paint.circle(, , r, fill="blue", outline=kontur)

# VINGARNA

paint.circle(r*3.5, r*6, r*gs, fill="white", outline=kontur)

# Fyll i x = 190
# Fyll i y = 220
# Multiplicera r med gs

#paint.circle(, , r, fill="blue", outline=kontur)

paint.circle(r*3.75, r*5, r*gs, fill="white", outline=kontur)
paint.circle(r*4.75, r*5, r*gs, fill="blue", outline=kontur)
paint.circle(r*3.75, r*4.25, r*gs, fill="white", outline=kontur)

# Fyll i x = 200
# Fyll i y = 180
# Multiplicera r med gs

#paint.circle(, , r, fill="blue", outline=kontur)

# STORA VITA CIRKEL

# Fyll i x = 240
# Fyll i y = 90
# Multiplicera r med gs och 2

#paint.circle(, , r, fill="white", outline=kontur)

# NÄBBEN

paint.circle_arc(r*7.75, r*4.75, r, fill="blue", outline=kontur, start=200, end=360)

paint.circle(r*8.15, r*4.25, r, fill="white", outline=kontur)

paint.circle_arc(r*7.5, r*4.35, r, fill="blue", outline=kontur, start=200, end=360)

# Fyll i x = 314
# Fyll i y = 150

#paint.circle(, , r, fill="white", outline=kontur)


# HUVUDET

# Fyll i x = 280
# Fyll i y = 210

#paint.circle(, , r, fill="blue", outline=kontur)


#-------------------------------------------------------------------------------

paint.drawPicture()
