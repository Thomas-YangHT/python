
import turtle as t, math

def drawline(x1,y1,x2,y2):
    t.pu()
    t.goto(x1,y1)
    t.pd()
    t.goto(x2,y2)
    t.pu()

def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        drawline(x1, y1, x2, y2)
        drawTree(x2, y2, angle - 20, depth - 1)
        drawTree(x2, y2, angle + 20, depth - 1)

if __name__ == '__main__':
    t.setup(600,600)
    t.pencolor('white')
    t.bgcolor('black')
    drawTree(0, -300, 90, 9)
    t.speed(10)
    t.exitonclick()

