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

    p = 0
    successful_cases = 0
    
    for gen in range(1, gens):
        if gen % 10 == 0:
            print("Generation :#%d" % gen)

        mutated = mutation.es_mutation(solution, minmax, p)
        #print(solution[0])
        #print(mutated[0])
        #print(list(map(operator.sub, mutated[0], solution[0])))

        fitness = common.fitness(mutated[0])

        if fitness <= best_fitness:
            best_fitness = fitness
            solution = mutated
            successful_cases += 1
            common.write_data(gen, fitness, 'es.dat')

        p = successful_cases / gen
        
        if fitness == 0:
            break

    print("#########################")
    print("# Strategy              : Evolutionary Strategies")
    print("# Generations           : " + str(gens))
    print("# Best Solution Fitness : %.3f" % best_fitness)
    print("# Log File              : ./es.dat")
    print("# Graph                 : Evolutionary_Strategies_Ackleys_Function.png")
    print("#########################")
    
    common.plot('Evolutionary Strategies: Ackleys Function', 'es.dat')

def genetic_algorithm(args):

    minmax = (args.min, args.max)
    N = args.N
    gens = args.gens

    solution = common.initialize(N,minmax)
    best_fitness = common.fitness(solution[0])

    for gen in range(1, gens):
        if gen % 10 == 0:
            print("Generation :#%d" % gen)

        mutated = mutation.ga_mutation(solution, minmax)
        fitness = common.fitness(mutated[0])

        if fitness <= best_fitness:
            best_fitness = fitness
            solution = mutated
            common.write_data(gen, fitness, 'ga.dat')

        if fitness == 0:
            break

    print("#########################")
    print("# Strategy              : Genetic Algorithms")
    print("# Generations           : " + str(gens))
    print("# Best Solution Fitness : %.3f" % best_fitness)
    print("# Log File              : ./ga.dat")
    print("# Graph                 : Genetic_Algorithm_Ackleys_Function.png")
    print("#########################")
    
    common.plot('Genetic Algorithm: Ackleys Function', 'ga.dat')
    
def main(args):

    if args.strategy == 'ga':
        data_file = 'ga.dat'
        if os.path.isfile(data_file):
            os.remove(data_file)
        genetic_algorithm(args)
    elif args.strategy == 'es':
        data_file = 'es.dat'
        if os.path.isfile(data_file):
            os.remove(data_file)
        evolutionary_strategies(args)
    else:
        print("Invalid Strategy, you can only choose 'ga' (Genetic Algorithms)"
              " or 'es' (Evolutionary Strategies)")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="N value for Ackley Function",
                        dest='N', type=int)
    parser.add_argument("--min", help="Minimal value", type=int)
    parser.add_argument("--max", help="Maximum value", type=int)
    parser.add_argument('-g', "--generations", help="Number of Generations",
                        dest='gens', type=int)
    parser.add_argument("--strategy", help="Strategy [ga|es]", type=str)

    args = parser.parse_args()
    
    main(args)
