#!/usr/bin/env python

import argparse
import numpy as np
import operator
import os

import common
import mutation


def evolutionary_strategies(args):

    minmax = (args.min, args.max)
    N = args.N
    gens = args.gens

    solution = common.initialize(N,minmax)
    best_fitness = common.fitness(solution[0])

    p = 1.5
    
    for gen in range(1, gens):
        #print("Generation :#%d" % gen)
        #if gen % 10 == 0:
        #    print("Generation :#%d" % gen)

        mutated = mutation.es_mutation(solution, minmax, p)
        #print(solution[0])
        #print(mutated[0])
        #print(list(map(operator.sub, mutated[0], solution[0])))

        fitness = common.fitness(mutated[0])

        if fitness <= best_fitness:
            best_fitness = fitness
            solution = mutated
            p = 1.5
        #elif fitness == best_fitness:
        #    p = 1
        else:
            p = 1.5 ** (-1/4)
            
        if fitness == 0:
            break

        common.write_data(gen, fitness, 'es.dat')
    
    common.plot('Auckey_with_Evolution_Srategies', 'es.dat')
    
def main(args):
    try:
        os.remove('es.dat')
    except Exception:
        pass

    evolutionary_strategies(args)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="N value for Ackley Function",
                        dest='N', type=int)
    parser.add_argument("--min", help="Minimal value", type=int)
    parser.add_argument("--max", help="Maximum value", type=int)
    parser.add_argument('-g', "--generations", help="Number of Generations",
                        dest='gens', type=int)

    args = parser.parse_args()
    
    main(args)
