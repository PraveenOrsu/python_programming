import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"distance between points({x1,y1}) and({x2,y2}) is{dist(x1,y1,x2,y2)}")