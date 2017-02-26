import random
import copy
import crossovers
import mutations
from individual import Individual


class Population:

    def __init__(self, individual, size=None):
        self.individuals = []
        chromosome = copy.copy(individual.chromosome)
        if size is None:
            self.size = len(individual.chromosome)
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
        while len(selected_individuals) < self.size/2:
            roulette = self.roulette()
            rnd = random.random()
            for index, value in enumerate(roulette):
                if rnd <= value:
                    selected_individuals.append(self.individuals[index])
                    self.individuals.pop(index)
                    break
        self.individuals = selected_individuals

    def crossover(self, pc):
        for index in range(0, len(self.individuals), 2):
            rnd = random.random()
            if rnd <= pc:
                child1, child2 = crossovers.aox_2(self.individuals[index].chromosome,
                                                  self.individuals[index+1].chromosome)
                self.individuals.append(Individual(child1))
                self.individuals.append(Individual(child2))

    def mutation(self):
        self.individuals[0] = Individual(mutations.rsm(self.individuals[0].chromosome))
