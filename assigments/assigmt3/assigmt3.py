#!/usr/bin/env python

import argparse
import numpy as np
import operator

import common
import mutation


def evolutionary_strategies(args):

    minmax = (args.min, args.max)
    N = args.N


    solution = common.initialize(N,minmax)
    #solution = ([1,1,1,1,1,1,1,1,1,1], [0,0,0,0,0,0,0,.5,.3,.2])
    best_fitness = common.fitness(solution[0])

    for gen in range(1, args.gens):
        #print("Generation :#%d" % gen)
        if gen % 100 == 0:
            print("Generation :#%d" % gen)

        mutated = mutation.es_mutation(solution, minmax)
        #print(solution[0])
        #print(mutated[0])
        #print(list(map(operator.sub, mutated[0], solution[0])))

        fitness = common.fitness(mutated[0])

        if fitness < best_fitness:
            best_fitness = fitness
            solution = mutated

            if fitness == 0:
                return
            
        #print(fitness)

    print("####################")
    print(solution[0])
    print(best_fitness)

    
def main(args):
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
