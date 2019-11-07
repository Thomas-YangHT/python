# coding: utf-8
from sincos import *     #ucs(x,y)画坐标系
from bidaTree import *   #drawSquare(x,y,l):画正方形
from fivestar import *   #Fstar(angle,length)画五角星  
                         #drawRectangle(x,y,l,rate)画矩形 
                         #savesvg(t,filename) 保存画布到svg文件
                         #svgedit(filename) 修改XML，替换evenodd为nonezero
from astroid import *    #draw_point_to_point(xlist,ylist) 按给定的x,y坐标列表画图

for i in range(1,30):
	drawSquare(0,0,i*5,0)
	#turtle.circle(i*5)
	#Fstar(10,i*10,0)
	turtle.right(15)
turtle.pu()
turtle.done()

