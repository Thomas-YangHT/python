#-*- coding: utf-8 -*-
#带文字弧图形
import turtle

t = turtle.Pen()
turtle.bgcolor("black")

my_name = u"飞车党"

colors = ["red", "yellow", "purple", "blue"]
for x in range(100):
    t.pencolor(colors[x % 4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(my_name.encode('utf-8'), font=("Arial", int((x + 4) / 4), "bold"))
    t.left(92)

turtle.exitonclick()
