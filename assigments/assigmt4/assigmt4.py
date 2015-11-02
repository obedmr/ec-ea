#!/usr/bin/env python

import argparse
import numpy as np
import operator
import os

import common
import mutation


def evolutionary_strategies(args):

    minmax = common.get_minmax(args.fitness)
    N = args.N
    gens = args.gens

    population = common.initialize(N,minmax)
    print(population[0])
    fittest, best_fitness = common.fittest(population[0],
                                           args.fitness)

    p = 0
    successful_cases = 0
    
    for gen in range(1, gens):
        if gen % (gens / 10) == 0:
            print("Generation :#%d" % gen)

        mutated = mutation.es_mutation(population, minmax, p)
        
        local_fittest, fitness = common.fittest(mutated[0],
                                                args.fitness)

        if fitness >= best_fitness:
            fittest = local_fittest
            best_fitness = fitness
            population = mutated
            successful_cases += 1
        common.write_data(gen, fitness, 'es.dat')

        p = successful_cases / gen

    print("#########################")
    print("# Strategy              : Evolutionary Strategies")
    print("# Generations           : " + str(gens))
    print("# Best Solution Value   : %.3f" % fittest)
    print("# Best Solution Fitness : %g" % best_fitness)
    print("# Log File              : ./es.dat")
    print("# Graph                 : Evolutionary_Strategies_%s.png" %
          args.fitness.upper())
    print("#########################")
    
    common.plot('Evolutionary Strategies %s' % args.fitness.upper(),
                'es.dat')

# (WORK in PROGRESS) Function (Don't use it)
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

        if fitness >= best_fitness:
            best_fitness = fitness
            solution = mutated
            common.write_data(gen, fitness, 'ga.dat')

    print("#########################")
    print("# Strategy              : Genetic Algorithms")
    print("# Generations           : " + str(gens))
    print("# Best Solution Fitness : %.3f" % best_fitness)
    print("# Log File              : ./ga.dat")
    print("# Graph                 : Genetic_Algorithm_Ackleys_Function.png")
    print("#########################")
    
    common.plot('Genetic Algorithm: Ackleys Function', 'ga.dat')
    
def main(args):

    fitness_functions = ['f2', 'f3', 'f5']
    fitness = args.fitness

    if fitness not in fitness_functions:
        print("You haven't specified the correct Fitness Functions")
        print("Available Functions: ")
        print(" | ".join(fitness_functions))
        return False
    
    if args.strategy == 'ga':
        data_file = 'ga.dat'
        if os.path.isfile(data_file):
            os.remove(data_file)
        #genetic_algorithm(args)
        print("This is a (Work In Progress Function)")
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
    parser.add_argument('-n', help="Population",
                        dest='N', type=int)
    parser.add_argument('-g', "--generations", help="Number of Generations",
                        dest='gens', type=int)
    parser.add_argument("--strategy", help="Strategy [ga|es]", type=str)
    parser.add_argument("-f", "--fitness", help="Fitness Function [f2|f3|f5]", type=str)
    
    args = parser.parse_args()
    
    main(args)
