
# coding: utf-8
import turtle as t, math

def drawSquare(x,y,l,f):
    if f==1: t.begin_fill()
    t.pu()
    t.goto(x,y)
    t.pd()
    for i in range(0,4):
        t.fd(l)
        t.right(90)
    t.end_fill()
    t.pu()

def bidaTree(x1, y1, depth,length,angle,forward):
    if depth:
        t.fillcolor(colors[depth-1])
        drawSquare(x1,y1,length)
        x1 = x1 + round(math.cos(angle*2*math.pi/360)*length)
        y1 = y1 + round(math.sin(angle*2*math.pi/360)*length)
        if forward == 'L':
            x2 = x1 + round(math.cos((angle-90)*2*math.pi/360)*length)
            y2 = y1 + round(math.sin((angle-90)*2*math.pi/360)*length)
        else:
            x2 = x1 + round(math.cos((angle+90)*2*math.pi/360)*length)
            y2 = y1 + round(math.sin((angle+90)*2*math.pi/360)*length)
        #print x1,y1,x2,y2,angle,forward,length
        length = math.sqrt(length**2/2)
        if forward == 'L':
            t.seth(angle + 45)
            bidaTree(x1, y1, depth - 1, length, angle+45, 'L')
            t.seth(angle + 45)
            bidaTree(x2, y2, depth - 1, length, angle-45, 'R')
        else:
            t.seth(angle + 45)
            bidaTree(x1, y1, depth - 1, length, angle-45, 'R')
            t.seth(angle + 45)
            bidaTree(x2, y2, depth - 1, length, angle+45, 'L')

def savesvg(t,filename):
    import canvasvg
    canvasvg.saveall(filename, t.getscreen().getcanvas())

t.setup(1000,800)
t.pencolor('white')
t.bgcolor('black')
t.hideturtle()
colors=["red","orange","pink","yellow","purple","coral","crimson","darkgoldenrod","chocolate","brown"] #每层的填充颜色
n = 10  #层数
l = 150  #矩形边长
t.tracer(False) #关闭画图动画过程
angle = 90 #直角
t.seth(angle) #设置画笔方向

if __name__ == '__main__':
    bidaTree(-l/2, -250, n, l, angle, 'L')
    savesvg(t,"bidaTree.svg")
    t.exitonclick()

