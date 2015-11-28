
import numpy as np
import random

import common

C = 0.817

def es_mutate_steps(steps, p):
    steps_size = len(steps)
    new_steps = []
    t1 = np.sqrt(2 * steps_size) ** -1 
    t2 = np.sqrt(2 * np.sqrt(steps_size)) ** -1 
    for idx,step in enumerate(steps):
        new_step = step * np.exp( (t1 * common.gaussian(0,1))
                                 + (t2 * common.gaussian(0,1)) )

        if p > 0.2:
            sigma = new_step / C
        elif p < 0.2:
            sigma = new_step * C
        else:
            sigma = new_step
            #sigma = new_step * p
        if sigma > 2:
            sigma = sigma % 2
        sigma = 1 - sigma
        
        new_steps.append(sigma)
    return new_steps

    
def es_mutate_population(population, steps, minmax):
    data = population[0]
    new_data = []

    #mutation_idx = random.randint(0, len(population))
    
    for idx,value in enumerate(data):
        new_value = value + (steps[idx] * common.gaussian(0,1))
        # Make sure mutated value no over passes max limit
        # We're not using negative values
        new_value = new_value % minmax[1]
        new_data.append(common.round(abs(new_value)))

    return (new_data, steps)
    

def es_mutation(population, minmax, p):
    new_steps = es_mutate_steps(population[1], p)
    new_population = es_mutate_population(population, new_steps, minmax)
    return new_population


def ga_mutation(individual, minmax):
    mutated = []
    mutation_idx = random.randint(0, len(individual[0])-1)
    mutation_delta =  round(random.uniform(-1,1),3)
    for idx,value in enumerate(individual[0]):
        if idx == mutation_idx:
            new_value = value + mutation_delta
        else:
            new_value = value
        mutated.append(new_value)
    return (mutated,None)

