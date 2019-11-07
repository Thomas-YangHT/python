import turtle as p

def wuhuan(R,x,y):
    p.pensize(3)
    colors=["blue","black","red","green","yellow"]
    dotx=[x,x+2*R,x+4*R,x+3*R,x+R]
    doty=[y,y,y,y-R,y-R]
    i=0
    for c in colors:
	    p.pu()
	    p.goto(dotx[i],doty[i])
	    p.pd()
	    p.color(c)
	    p.circle(R,360)
	    i+=1

R = 30
x = 0-2*R
y = 100
if __name__ == "__main__":
    wuhuan(R,x,y)
    import canvasvg
    canvasvg.saveall("wuhuan.svg", p.getscreen().getcanvas())


#old code:
p.pu()
p.goto(0,0)
p.pd()
p.color("blue")
p.circle(R, 360)
p.pu()
p.goto(2*R, 0)
p.pd()
p.color("black")
p.circle(R, 360)
p.pu()
p.goto(4*R, 0)
p.pd()
p.color("red")
p.circle(R, 360)
p.pu()
p.goto(3*R, -R)
p.pd()
p.color("green")
p.circle(R, 360)
p.pu()
p.goto(R, -R)
p.pd()
p.color("yellow")
p.circle(R, 360)

p.done()
