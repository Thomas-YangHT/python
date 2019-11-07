# coding: utf-8
from sincos import *     #ucs(x,y)画坐标系
from bidaTree import *   #drawSquare(x,y,l):画正方形
from fivestar import *   #Fstar(angle,length)画五角星  
                         #drawRectangle(x,y,l,rate)画矩形 
                         #savesvg(t,filename) 保存画布到svg文件
                         #svgedit(filename) 修改XML，替换evenodd为nonezero

def astroid(xi,a):       #星形曲线
	import math
	"""
	#方法1，边计算坐标点，边画图
	a=math.pow(a,2.0/3)
	turtle.pencolor("yellow")
	turtle.fillcolor("orange")
	lenx=len(list(range(-xi,xi)))+1
	i=0
	for x in list(range(-xi,xi))+list(range(xi,-xi,-1)) :
		y=a-math.pow(x**2,1.0/3)
		y=math.pow(y,3.0/2)
		if i<lenx: 
			turtle.goto(x,y)
		elif i>lenx:
			turtle.goto(x,-y)
		if x == -xi : 
			turtle.pd()
			turtle.begin_fill()			
		i+=1
		#print(a,x,y)
		#print(a,x,-y)
	turtle.end_fill()
	"""
	#方法2，先保存坐标点数据，最后再画图
	a=math.pow(a,2.0/3)
	dic1={'x':[],'y':[]}
	dic2={'x':[],'y':[]}
	for x in range(-xi,xi):
		y=a-math.pow(x**2,1.0/3)
		y=math.pow(y,3.0/2)
		dic1['x'].append(x)
		dic1['y'].append(y)
		dic2['x'].append(x)
		dic2['y'].append(-y)
	dic2['x'].reverse()
	dic2['y'].reverse()
	dic1['x']+=dic2['x']
	dic1['y']+=dic2['y']
	draw_point_to_point(dic1['x'],dic1['y'])

def draw_point_to_point(xlist,ylist):
	#print(xlist,ylist)
	turtle.pencolor('blue')
	turtle.fillcolor("orange")
	turtle.pu()
	turtle.pensize(1)
	turtle.goto(xlist[0],ylist[0])
	turtle.pd()
	turtle.begin_fill()	
	for x,y in zip(xlist,ylist):
		turtle.goto(x,y)
		#print(x,y)
	turtle.end_fill()

if __name__ == '__main__':
	ucs(300,220)
	astroid(200,200)
	savesvg(t,"starxing.svg")
	turtle.hideturtle()
	turtle.done()