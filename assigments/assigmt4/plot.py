#!/bin/env python3

import common

# Function 2 and 3
f2 = open('f2.dat', 'w')
f3 = open('f3.dat', 'w')

for x in range(0,20000):
    fitness_f2 = common.fitness(x * 0.001, 'f2')
    fitness_f3 = common.fitness(x * 0.001, 'f3')
    f2.write("%d, %.3f\n" % (x, fitness_f2))
    f3.write("%d, %.3f\n" % (x, fitness_f3))
    
f2.close()
f3.close()

common.plot('F2', 'f2.dat')
common.plot('F3', 'f3.dat')

# Function 5
f5 = open('f5.dat', 'w')

for x in range(0,1000):
    fitness_f5 = common.fitness(x * 0.001, 'f5')
    f5.write("%d, %f \n" % (x, fitness_f5))
    
f5.close()

common.plot('F5', 'f5.dat')
