import random
import copy
import numpy as np
import crossovers
import mutations
from individual import Individual


class Population:

    cp = 0.9
    mp = 0.015

    def __init__(self, individual, size=None):
        self.individuals = []
        chromosome = copy.copy(individual.chromosome)
        if size is None:
            self.size = len(chromosome) + 1
        else:
            self.size = size
        while len(self.individuals) < self.size:
            random.shuffle(chromosome)
            if chromosome not in self.individuals:
                self.individuals.append(Individual(copy.copy(chromosome)))

    def fitness_sum(self):
        fitness_sum = 0
        for individual in self.individuals:
            fitness_sum += individual.fitness()
        return fitness_sum

    def roulette(self):
        fitness_sum = self.fitness_sum()
        roulette = [(1 - float(self.individuals[0].fitness())/fitness_sum)/(self.size - 1)]
        for index in range(1, len(self.individuals)):
            roulette.append((1 - float(self.individuals[index].fitness())/fitness_sum)/(self.size - 1) +
                            roulette[index-1])
        return roulette

    def selection(self):

        selected_individuals = []
        fitness_mean = np.mean([indiv.fitness() for indiv in self.individuals])

        for ind in self.individuals:
            ind.set_quorem(fitness_mean)
        population_bis = copy.deepcopy(self)

        for i in range(self.size):
            roulette = self.roulette()
            rnd = random.random()
            for index, value in enumerate(roulette):
                if rnd <= value:
                    for j in range(self.individuals[index].quotient):
                        selected_individuals.append(self.individuals[index])
                    self.individuals.pop(index)
                    break

        cpt = 0
        while len(selected_individuals) < population_bis.size:
            rnd_list = random.randint(0, len(population_bis.individuals) - 1)
            rnd_remain = random.random()
            if population_bis.individuals[rnd_list].remainder >= rnd_remain or cpt >= 10:
                selected_individuals.append(population_bis.individuals[rnd_list])
                population_bis.individuals.pop(rnd_list)
            cpt += 1

        self.individuals = selected_individuals

    def crossover(self):
        new_generation = [self.fittest()]
        for index in range(len(self.individuals) - 1):
            rnd = random.random()
            if rnd <= Population.cp:
                child = crossovers.aox(self.individuals[index].chromosome, self.individuals[index+1].chromosome)
                new_generation.append(Individual(child))
            else:
                if rnd <= 0.5:
                    new_generation.append(self.individuals[index])
                else:
                    new_generation.append(self.individuals[index+1])
        rnd = random.random()

        # crossover du dernier et premier
        if rnd <= Population.cp:
            child = crossovers.aox(self.individuals[-1].chromosome, self.individuals[0].chromosome)
            new_generation.append(Individual(child))
        else:
            if rnd <= 0.5:
                new_generation.append(self.individuals[-1])
            else:
                new_generation.append(self.individuals[0])

        self.individuals = new_generation

    def mutation(self):
        for individual in self.individuals:
            rnd = random.random()
            if rnd <= Population.mp:
                mutations.rsm(individual.chromosome)

    def fittest(self):
        elite = self.individuals[0]
        elite_fitness = self.individuals[0].fitness()

        for index in range(1, len(self.individuals)):
            fitness = self.individuals[index].fitness()
            if fitness < elite_fitness:
                elite = self.individuals[index]
                elite_fitness = fitness
        return elite

    def __str__(self):
        individuals = []
        for ind in self.individuals:
            individuals.append(ind.__str__())
        return '\n'.join(individuals)
