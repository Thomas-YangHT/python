# coding: utf-8
# 绘制围棋棋盘

import turtle

# 线与线间隔
n = 30
# 初始点位置
x = -300
y = -300

# 定义棋盘样式
turtle.speed(3)
turtle.pencolor('black')
turtle.screensize(400, 400)

# 画横线
for i in range(19):
    turtle.penup()
    turtle.goto(x, y + n * i)
    turtle.pendown()
    turtle.forward(n * 18)

# 画竖线
turtle.left(90)
for i in range(19):
    turtle.penup()
    turtle.goto(x + n * i, y)
    turtle.pendown()
    turtle.forward(n * 18)

turtle.right(90)

# 画9个星位，每排三个，共三排所以是两层for循环
x_first = x + n * 3
y_first = y + n * 3 - n * 0.25

for i in range(3):
    for j in range(3):
        turtle.penup()
        turtle.goto(x_first + 6 * j * n, y_first + 6 * i * n)
        # 如果按下面写法，则先画左边3个星，再画中间3个
        # turtle.goto(x_first + 6 * j * n, y_first + 6 * i * n)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor('blue')
        # 飞星的半径为1/4个网格间距
        turtle.circle(n * 0.25)
        turtle.end_fill()

# 隐藏画笔箭头
turtle.hideturtle()

turtle.done()