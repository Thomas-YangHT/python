# coding=utf-8
import turtle as t
import time

def savesvg(t,filename):
    import canvasvg
    canvasvg.saveall(filename, t.getscreen().getcanvas())

def drawRectangle(x,y,l,rate):  #rate 长宽比
    t.begin_fill()
    t.color("red")
    t.pu()
    t.goto(x,y)
    t.pd()
    for i in range(0,4):
        t.fd(l) if i%2==0 else t.fd(l*rate)
        t.right(90)
    t.end_fill()
    t.pu()

def Fstar(angle,length,f):
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.right(angle)
    if f==1: t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()

def fivestar():
	x     =[-420,-180,-130,-140,-180]
	y     =[150 ,220 ,160 ,70  ,10  ]
	angles=[0   ,15  ,25  ,-40 ,15  ]
	R1=200
	R2=50
	for i in range(0,5):
		R=200 if i==0 else 50
		t.penup()
		t.goto(x[i],y[i])
		Fstar(angles[i],R,1)
	t.up()

def svgedit(filename):  #将polygon元素fill-rule属性从evenodd改为nonezero
	import re
	import xml.etree.ElementTree as ET
	tree = ET.parse(filename)
	root = tree.getroot()
	for element in root:
	    tag = element.tag #访问Element标签
	    if  re.match(r".*polygon.*",tag): element.attrib['fill-rule']='nonezero' 
	tree.write(filename)		

if __name__ == '__main__':
	t.screensize(900,600, "red")
	t.setup(900,600)
	t.bgcolor('red')
	t.pensize(5)
	t.hideturtle()
	t.tracer(False)
	t.seth(90)
	drawRectangle(-450,-300,600,1.5)
	t.seth(0)
	fivestar()
	savesvg(t,"fivestar.svg")
	svgedit("fivestar.svg")
	t.exitonclick()