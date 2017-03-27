import csv
from individual import Individual
from population import Population
from gene import Gene


chromosome = []
with open('dataset.csv') as datasetFile:
    dataset = csv.reader(datasetFile, delimiter=',')
    line = dataset.next()
    init_city = Gene(line[0], int(line[1]), int(line[2]))
    Gene.init(init_city)
    for row in dataset:
        chromosome.append(Gene(row[0], int(row[1]), int(row[2])))

individual = Individual(chromosome)
print individual

population = Population(individual, 50)
print population
