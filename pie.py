import random
import math

size = 100.0 #input('size: \n')
factor = input('sample: ')
points = 10.0*factor

hit = 0
line = 0 


def distance(x,y):
    random.seed()
    tmp = x**2 + y**2
    print x
    print y 
    #print ",",  math.sqrt(tmp)
    return math.sqrt(tmp)

i = 0.0
while i <= points:
    x = random.uniform(0,size)
    y = random.uniform(0,size)
    
    if distance(x,y) <= size :
        hit += 1
        if distance(x,y) == size:
            line += 1
    i += 1

 
result = float(hit)/points

print "on the line", line

print "hit: ", hit
print "points", points
print "pie: ", result
