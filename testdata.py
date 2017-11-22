# Nathan Timmerman 
# November 2017

# Test data sets with verious functions
# Data set is provided as file name from cmd line argument 
# Expected data delimited by line feed \n

#import statistics
import sys
import math 

def make_list (file_name):   # create and return float array from data file 
    list = []
    with open(file_name) as file:
        for line in file:
            list.append(float(line))
    file.close()
    return list


def output_list(list):
    with open(output_file, "w") as file:
        for i in list:
            file.write(str(i)+"\n")
    file.close()


def distribution( dataset, mode ): #analize distribution by counting occurnces # return list fraction of whole
    list = []
    precentage = []
    for i in range(mode):       # [0, mode] itteration
        list.append(0)          #list of 0 size mode
    for n in dataset:
        index = n   # math.floor() returns float
        print index
        list [index] +=1   # count 
    total = sum(dataset)
    for j in list:
        precentage.append((j/total)*1000)
    return precentage


def average (set):    # returns float
    avg = sum(set)/len(set)
    return avg



input_file = sys.argv[1] 
output_file = sys.argv[2]
data = make_list(input_file)
output_list(sorted(data))



print average(data)
print distribution(data, 10)
