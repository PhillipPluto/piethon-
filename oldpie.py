import random
import math

size = 10.0#input('size: \n')                                                                               
factor = input('sample: ')
points = 10.0**factor

hit = 0
line = 0


file = open("dataset", "w")



def distance(x,y):
    tmp = float(x)**2 + float(y)**2
    #print ",",  math.sqrt(tmp)                                                                             
    #print x
    #print y
    return math.sqrt(tmp)

i = 0.0
while i <= points:
    #state = random.getstate()
    x = random.randint(0,size)
    y = random.randint(0,size)
    file.write(str(x)+"\n")
    file.write(str(y)+"\n")

    if distance(x,y) <= size :
        hit += 1
        if distance(x,y) == size:
            line += 1
    i += 1


miss = points - hit
result = float(hit)/miss

print "on the line", line

print "hit: ", hit
print "miss: ", miss
print "pie: ", result
