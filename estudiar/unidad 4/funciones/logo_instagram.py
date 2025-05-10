#logo de instagram
#import turtle
from turtle import *
bgpic("Background.png")
pencolor("white")
width(23)
penup()
hideturtle()
goto(160, -100)
pendown()

left(90)
for j in range(4):
    forward(250)
    circle(34, 90)
penup()
goto(85, 30)
pendown()
circle(80, 360)
penup()
goto(110, 130)
pendown()
circle(7, 360)
turtles.mainloop()    