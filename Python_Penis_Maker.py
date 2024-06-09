import turtle
import math
from tkinter import *
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askfloat

girth = askinteger("Input", "What girth would you like?")
length = askinteger("Input", "What length would you like?")
curve = askfloat("Input", "How steep of a curve would you like? (the higher the number the steeper the curver, 1 = default, MAX = 10, MIN = 0.1")
ballradius = askinteger("Input", "What size balls would you like?")
penwidth = askinteger("Input", "What width pen would you like (max 5)")
if penwidth > 5:
    root = Tk()
    text = Text(root)
    text.insert(INSERT, "Invalid pen width maximum is 5!")
    text.pack()
    root.mainloop()
    exit()
color = askstring("Input", "What colour penis would you like? (Pink, Black or Blue)")
if color.lower() == 'black':
    turtle.color('#000000')
elif color.lower() == 'pink':
    turtle.color('#fe0099')
elif color.lower() == 'blue':
    turtle.color('#1d3ffe')
else:
    root = Tk()
    text = Text(root)
    text.insert(INSERT, "Invalid colour type (can only be: pink, black or blue!)")
    text.pack()
    root.mainloop()
    exit()
if curve > 10 or curve < 0.1:
    root = Tk()
    text = Text(root)
    text.insert(INSERT, "Invalid curve of the shaft! Must be between 10 or 0.1!")
    text.pack()
    root.mainloop()
    exit()

turtle.pensize(penwidth)
turtle.title("Penis Drawer 2000")
for x in range(1, int(length)):
    turtle.goto((x),((curve * 0.01)*(x * x)))
savex = turtle.xcor()
savey = turtle.ycor()
turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()
turtle.setpos(-abs(int(girth)), int(girth))
for z in range(1, int(length)):
    turtle.goto((int(z) - int(girth)), int((curve * 0.01) * (z * z) + int(girth)))
savexcircle = turtle.xcor()
saveycircle = turtle.ycor()
turtle.goto(float(savex), float(savey))
turtle.penup()
turtle.goto(float(savexcircle), float(saveycircle))
turtle.pendown()
midpointx = (savexcircle + (savex- savexcircle)/2)
midpointy = (saveycircle + (savey - saveycircle)/2)
radiusx = (savex - midpointx)
radiusy = (savey - midpointy)
#origin =
#radius = math.sqrt((radiusx * radiusx) + (radiusy * radiusy))
radius = (savex - savexcircle)
for u in range(savexcircle, (savex +1 )):
    #y^2-2ky-zconstant=0
    #(u-midpointx)^2 + (y-midpointy)^2 = radius^2
    ycirclenum = float(math.sqrt(abs((radius * radius) - ((u - savexcircle) * (u - savexcircle)))) + savey)
    turtle.goto(float(u), float(ycirclenum))
turtle.goto(savex, savey)
turtle.penup()
turtle.goto(0, -abs(ballradius))
turtle.pendown()
turtle.circle(int(ballradius))
girthcoorx = -abs(int(girth))
girthcoory = int(girth)
turtle.penup()
turtle.goto(girthcoorx, int(girthcoory - ballradius))
turtle.pendown()
turtle.circle(int(ballradius))
turtle.hideturtle()
print("Penis is complete!")




turtle.exitonclick()


