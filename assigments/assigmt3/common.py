
import math
import numpy as np
import random


def initialize(population, minmax):
    minmax_diff = minmax[1] - minmax[0]
    values = [float("%.2f" % x)
              for x in np.random.ranf(population) * minmax_diff - minmax[1]]
    steps = [float("%.2f" % x)
              for x in np.random.ranf(population)]
    return values, steps
    

def gaussian(mean, stdv):
    return np.random.normal(mean, stdv)
    #u1 = u2 = w = 1
    #while(w >= 1): 
    #    u1 = 2 * np.random.uniform() - 1
    #    u2 = 2 * np.random.uniform() - 1
    #    w = u1 * u1 + u2 * u2
    #     
    #w = np.sqrt((-2.0 * np.log(w)) / w)
    #return round(mean + (u2 * w) * stdv)


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
