# coding=utf-8
# 在正交坐标系下画sin(x)和cos(x)曲线

import turtle
import math

def draw_line(t,x1, y1, x2, y2):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.speed(6)
    t.goto(x2, y2)

def draw_aron(angle,x,y):
	#画箭头
	turtle.setheading(150+angle)
	turtle.forward(20)
	turtle.penup()
	turtle.goto(x,y)
	turtle.setheading(-150+angle)
	turtle.pendown()
	turtle.forward(20)

def write_text(x,y,text):
	#标注X or Y
	turtle.penup()
	turtle.goto(x+25, 0) if x>y else turtle.goto(0,y+10) 
	turtle.write(text)	

def ucs(x,y):
	# 画 x 轴
	draw_line(turtle,-x,0,x,0)
	# 画 x 轴箭头
	draw_aron(0,x,0)
	write_text(x,0,"X")
	# 画 y 轴
	draw_line(turtle,0,-y,0,y)
	# 画 y 轴箭头
	draw_aron(90,0,y)
	write_text(0,y,"Y")


def sincos(xa,y):
	# 画正弦曲线
	turtle.pensize(2)
	turtle.color('blue')
	turtle.penup()
	turtle.goto(-xa, int(y/2 * math.sin(-xa * 2 * math.pi / 360)))
	turtle.pendown()
	for x in range(-xa, xa+1):
		turtle.goto(x, y/2 * math.sin(x * 2 * math.pi / 360))
		#print int(y/2 * math.sin(x * 2 * math.pi / 360))

	# 将-2π的位置标示出来
	write_text(-100,-20,"-2π")
	# 将2π的位置标示出来
	write_text(100,-20,"2π")

	# 画余弦曲线
	turtle.pensize(2)
	turtle.color('red')
	turtle.penup()
	turtle.goto(-xa, y/2 * math.cos(-xa * 2 * math.pi / 100))
	#print y/2 * math.cos( -175 * 2 * math.pi / 360)
	#print y/2 * math.cos( 176 * 2 * math.pi / 360)
	turtle.pendown()
	for x in range(-xa, xa+1):
		turtle.goto(x, int(y/2 * math.cos( x * 2 * math.pi / 100)) )
		#print float(x)/100
		#print x * 2 * math.pi / 360
		#print int(y/2 * math.cos( x * 2 * math.pi / 360))

if __name__ == '__main__':
	turtle.speed(5)
	turtle.setup(900,600)
	#axis(175,100)
	#sincos(175,100)
	ucs(400,250)
	sincos(400,250)

	turtle.hideturtle()
	turtle.done()
