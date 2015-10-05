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
    best_fitness = common.fitness(solution[0])

    for gen in range(1, args.gens):
        #print("Generation :#%d" % gen)
        #print(solution[0])
        #print(solution[1])
        mutated = mutation.es_mutation(solution, minmax)
        fitness = common.fitness(mutated[0])

        solution = mutated

        if fitness < best_fitness:
            best_fitness = fitness
        
        #print(fitness)

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
