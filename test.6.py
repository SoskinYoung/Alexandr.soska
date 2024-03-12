from turtle import *

bgcolor("black")

colors = ["red", "green", "blue", "violet"]
pencolor("white")

width(20)

def draw_spiral():
    for i in range(360):
        forward(20)  
        right(15)   
        pencolor(colors[i % len(colors)])  

hideturtle()

draw_spiral()

exitonclick()
