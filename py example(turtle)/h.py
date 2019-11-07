# coding=utf-8

import turtle as t
import random

def set_screen():
    t.setup(1000,800)
    t.pu()
    t.hideturtle()
    t.pensize(3)
    t.colormode(255)

def draw_line(x1, y1, x2, y2):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.speed(6)
    t.goto(x2, y2)
    t.pu()

def draw_H(x, y, l):
    line_a = [[x - l/2, y + l/2], [x - l/2, y - l/2]]
    line_b = [[x - l/2, y], [x + l/2, y]]
    line_c = [[x + l/2, y + l/2], [x + l/2, y - l/2]]
    t.pencolor([random.randint(0,255) for i in range(3)])    # 随机画笔的颜色
    draw_line(line_a[0][0], line_a[0][1], line_a[1][0], line_a[1][1])
    draw_line(line_b[0][0], line_b[0][1], line_b[1][0], line_b[1][1])
    draw_line(line_c[0][0], line_c[0][1], line_c[1][0], line_c[1][1])

def tree_H(n, x, y, l):
    if n == 0:    return                       # 当 n == 0 时，什么也不画
    draw_H(x,y,l)                           # 调用 draw_H 绘制一个 H 树
    tree_H(n-1, x - l/2, y + l/2, l/2)      # 每一个 H 有四个顶点，所以有四个自身调用
    tree_H(n-1, x - l/2, y - l/2, l/2)
    tree_H(n-1, x + l/2, y + l/2, l/2)
    tree_H(n-1, x + l/2, y - l/2, l/2)

def main():
    set_screen()
    #t.tracer(False)
    tree_H(4, 0, 0, 300)
    t.done()
    #t.tracer(True)

if __name__ == '__main__':   main()
