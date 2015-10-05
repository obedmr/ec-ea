
import numpy as np

import common

def es_mutate_steps(steps):
    steps_size = len(steps)
    new_steps = []
    t1 = np.sqrt(2 * steps_size) ** -1 
    t2 = np.sqrt(2 * np.sqrt(steps_size)) ** -1 
    
    for idx,step in enumerate(steps):
        new_step = step * np.exp( (t1 * common.gaussian(0,1))
                                 + (t2 * common.gaussian(0,1)) )
        if new_step < -1 or new_step > 1:
            new_step = step
            
        new_steps.append(new_step)
    return new_steps

    
def es_mutate_individual(individual, steps, minmax):
    data = individual[0]
    new_data = []

    for idx,value in enumerate(data):
        new_value = value + (steps[idx] * common.gaussian(0,1))
        if new_value > minmax[1]: 
            new_value = minmax[0]
        if new_value < minmax[0]:
            new_value = minmax[1]
        new_data.append(common.round(new_value))

    return (new_data, steps)
    

def es_mutation(individual, minmax):
    new_steps = es_mutate_steps(individual[1])
    new_individual = es_mutate_individual(individual, new_steps, minmax)
    print()
    print(new_individual[0])
    return new_individual


def ga_mutation(individual, minmax):
    pass
