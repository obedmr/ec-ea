
import math
import numpy as np
import random

import matplotlib.pyplot as plt
from pylab import *


def initialize(population, minmax):
    minmax_diff = minmax[1] - minmax[0]
    values = [round(x)
              for x in np.random.ranf(population) * minmax[1]]
    steps = [float("%.3f" % x)
              for x in np.random.ranf(population)]
    return values, steps


def get_minmax(function):
    # Functions f2, f3
    minmax = 0 , 20
    if function == 'f5':
        minmax = 0 , 1
        
    return minmax


def gaussian(mean, stdv):
    return np.random.normal(mean, stdv)


def round(value):
    return float('%.3f' % value)


def fitness(x, function):
    result = 0
    if function == 'f2':
        if x >= 0 and x < 15:
            result = ( 160 * (15 - x) ) / 15
        if x >= 15 and x <= 20:
            result = ( 200 * (x - 15) ) / 5
    elif function == 'f3':
        if x >= 0 and x < 10:
            result = ( 160 * x ) / 10
        if x >= 10 and x < 15:
            result = ( 160 * ( 15 - x ) ) / 5
        if x >= 15 and x <= 20:
            result = ( 200 * ( x - 15 ) ) / 5
    elif function == 'f5':
        if x >= 0 and x <= 1:
            result = math.sin( 5 * math.pi * x ) ** 6

    return result 


def fittest(poblation, function):
    fittest = 0
    best_fitness = 0

    for value in poblation:
        local_fitness = fitness(value, function)
        if local_fitness >= best_fitness:
            best_fitness = local_fitness
            fittest = value

    return fittest, best_fitness


def exchange(plist, nexchange):
    new_plist = []
    for i in range(0, nexchange):
        ind_idx = np.random.randint(1, len(plist[0][0]) - 1)
        for idx,population in enumerate(plist):
            new_plist.append(population)
            new_plist[idx][0][ind_idx] = population[0][ind_idx]
            
    return new_plist

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
    plt.clf()
