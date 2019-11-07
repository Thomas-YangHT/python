# coding=utf-8
#科勒曲线
import turtle

def coch_a(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            coch_a(size / 3, n - 1)

def coch(level):
    coch_a(400, level)
    turtle.right(120)
    coch_a(400, level)
    turtle.right(120)
    coch_a(400, level)
    turtle.hideturtle()

if __name__ == '__main__':
    turtle.tracer(False)
    turtle.setup(600, 600)
    turtle.penup()
    turtle.bgcolor("white")
    turtle.pensize(2)
    turtle.pencolor('red')
    turtle.goto(-200, 100)
    turtle.speed(5)
    turtle.pendown()
    coch(3)
    turtle.pu()
    ts = turtle.getscreen().getcanvas() #.postscript(file="coch.eps") #.eps文件即postscript脚本    
    import canvasvg
    canvasvg.saveall("coch.svg", ts)
  #  import cairosvg
  #  with open("coch.svg") as svg_input, open("coch.png", 'wb') as png_output:  # svg转换png
  #      cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
    turtle.tracer(True)
    turtle.exitonclick()
