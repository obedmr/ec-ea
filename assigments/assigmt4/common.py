
import math
import numpy as np
import random

import matplotlib.pyplot as plt
from pylab import *


def initialize(population, minmax):
    minmax_diff = minmax[1] - minmax[0]
    values = [round(x)
              for x in np.random.ranf(population) * minmax_diff - minmax[1]]
    steps = [float("%.2f" % x)
              for x in np.random.ranf(population)]
    return values, steps
    

def gaussian(mean, stdv):
    return np.random.normal(mean, stdv)


def round(value):
    return float('%.3f' % value)


def fitness(data, c1=20.0, c2=0.2, c3=2*math.pi):
    sum1 = 0.0
    sum2 = 0.0
    N = len(data)
    for value in data:
        sum1 += value ** 2.0
        sum2 += math.cos(c3 * value)

    result = -c1 * np.exp(-c2 * np.sqrt(sum1 / N)) - np.exp(sum2 / N) + c1  + math.e
    #print(sum1,sum2,result)
    #result = 0
    #for value in data:
    #    result += value ** 2
    return round(result) 

def write_data(generation, fitness, filename):
    f = open(filename, 'a')
    f.write('%d, %.3f\n' % (generation, fitness))
    f.close()


def plot(title_str, filename):
    # Read the file.
    f2 = open(filename, 'r')
    # read the whole file into a single variable,
    # which is a list of every row of the file.
    lines = f2.readlines()
    f2.close()
    
    # initialize some variable to be lists:
    x1 = []
    y1 = []
    
    # scan the rows of the file stored in lines,
    # and put the values into some variables:
    for line in lines:
        p = line.split(',')
        x1.append(p[0])
        y1.append(float(p[1]))

    xv = np.array(x1)
    yv = np.array(y1)
    
    # now, plot the data:
    plt.plot(xv, yv)
    
    # Set up
    xlabel('Iterations')
    ylabel('Value')
    title(title_str)
    grid(True)
    
    savefig('%s.png'% title_str.replace(':', '').replace(' ', '_'))
    
