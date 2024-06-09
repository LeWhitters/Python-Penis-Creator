import turtle
import math
girth = input("How girthy?")
length = input("How long?")
ballradius = int(input("How large testes?"))
for x in range(1, int(length)):
    turtle.goto((x),(0.01*(x * x)))
savex = turtle.xcor()
savey = turtle.ycor()
turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()
turtle.setpos(-abs(int(girth)), int(girth))
for z in range(1, int(length)):
    turtle.goto((int(z) - int(girth)), int(0.01 * (z * z) + int(girth)))
savexcircle = turtle.xcor()
saveycircle = turtle.ycor()
turtle.goto(float(savex), float(savey))
turtle.penup()
turtle.goto(float(savexcircle), float(saveycircle))
turtle.pendown()
midpointx = (savexcircle + (savex- savexcircle)/2)
print(midpointx)
midpointy = (saveycircle + (savey - saveycircle)/2)
print(midpointy)
radiusx = (savex - midpointx)
radiusy = (savey - midpointy)
#origin =
#radius = math.sqrt((radiusx * radiusx) + (radiusy * radiusy))
radius = (savex - savexcircle)
print(radius)
for u in range(savexcircle, savex):
    #y^2-2ky-zconstant=0
    #(u-midpointx)^2 + (y-midpointy)^2 = radius^2
    ycirclenum = float(math.sqrt(abs((radius * radius) - ((u - savexcircle) * (u - savexcircle)))) + savey)
    turtle.goto(float(u), float(ycirclenum))
turtle.penup()
turtle.goto(0, 0)
for ball1 in range(0, int(ballradius)):
    bally = abs(int(math.sqrt(abs(ballradius * ballradius) - (ball1 * ball1))))
    turtle.goto(float(ball1), float(bally))
    turtle.pendown()
turtle.penup()
for ball2 in range(-abs(ballradius), 0):
    bally = abs(float(math.sqrt(abs((ballradius * ballradius)) - (ball2 * ball2))))
    turtle.goto(ball2, float(bally))
    turtle.pendown()
turtle.penup()
for ball3 in range(0, ballradius):
    bally = -abs(float(math.sqrt(abs((ballradius * ballradius)) - (ball3 * ball3))))
    turtle.goto(ball3, float(bally))
    turtle.pendown()
turtle.penup()
for ball4 in range(-abs(ballradius), 0):
    bally = -abs(float(math.sqrt(abs((ballradius * ballradius)) - (ball4 * ball4))))
    turtle.goto(ball4, float(bally))
    turtle.pendown()
turtle.penup()
girthcoorx = -abs(int(girth))
girthcoory = int(girth)
turtle.setpos(girthcoorx, girthcoory)
for ball5 in range(girthcoorx, int(ballradius + girthcoorx)):
    bally = float(math.sqrt(abs((ballradius * ballradius) - ((ball5 - girthcoorx) * (ball5 - girthcoorx)))) + girthcoory)
    turtle.goto(float(ball5), float(bally))
    turtle.pendown()
turtle.penup()
for ball6 in range((girthcoorx - ballradius), girthcoorx):
    bally = float(math.sqrt(abs((ballradius * ballradius) - ((ball6 - girthcoorx) * (ball6 - girthcoorx)))) + girthcoory)
    turtle.goto(float(ball6), float(bally))
    turtle.pendown()
turtle.penup()
for ball7 in range(girthcoorx, int(ballradius + girthcoorx)):
    bally = -abs(float(math.sqrt(abs((ballradius * ballradius) - ((ball7 - girthcoorx) * (ball7 - girthcoorx)))) + girthcoory)) + (girthcoory + girthcoory)
    turtle.goto(float(ball7), float(bally))
    turtle.pendown()
turtle.penup()
for ball8 in range((girthcoorx - ballradius), girthcoorx):
    bally = -abs(float(math.sqrt(abs((ballradius * ballradius) - ((ball8 - girthcoorx) * (ball8 - girthcoorx)))) + girthcoory)) + (girthcoory + girthcoory)
    turtle.goto(float(ball8), float(bally))
    turtle.pendown()
turtle.penup()




turtle.exitonclick()


