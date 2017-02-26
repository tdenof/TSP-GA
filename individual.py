import numpy as np
import random


class Individual:

    cities = []
    distances = np.matrix('')
    indexes = {}

    def __init__(self, chromosome):
        self.chromosome = chromosome

    @staticmethod
    def init(cities, distances):
        Individual.cities = cities
        Individual.distances = distances
        Individual.indexes = dict(zip(cities, range(len(cities))))

    def fitness(self):
        distance = 0
        for i in range(len(self.chromosome) - 1):
            distance += Individual.distances[Individual.indexes[self.chromosome[i]],
                                             Individual.indexes[self.chromosome[i + 1]]]
        return distance

    def selected(self, fitness_sum):
        probability = float(self.fitness())/fitness_sum
        rnd = random.random()
        print probability
        print rnd
        if probability <= rnd:
            return True
        else:
            return False
