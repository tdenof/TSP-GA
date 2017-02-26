import numpy as np
import csv
from individual import Individual
from population import Population


cities = []
indexes = {}
distances = []
with open('dataset.csv') as datasetFile:
    dataset = csv.reader(datasetFile, delimiter='\t')
    cities = dataset.next()[1:]
    indexes = dict(zip(cities, range(len(cities))))
    for row in dataset:
        distances.append(map(lambda data: int(data), row[1:]))
    distances = np.matrix(distances)


print cities
print distances
print indexes

individual = Individual(cities)
Individual.init(cities, distances)

population = Population(individual)
print individual.chromosome
print individual.fitness()
print map(lambda instance: instance.fitness(), population.individuals)
fitness_sum = population.fitness_sum()
print fitness_sum
print map(lambda instance: instance.chromosome, population.individuals)
population.selection()
print map(lambda instance: instance.chromosome, population.individuals)
population.crossover(0.75)
# population.mutation()
print map(lambda instance: instance.chromosome, population.individuals)
