import turtle as t
import math

def fab(target):
    #target=30
    a,b=0,1
    for i in range(target):
        print a,
        a,b=b,a+b
        if a<1024000: t.circle(math.sqrt(a),90) 
    print a,b

#fab(30)
#t.done()