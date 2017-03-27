from gene import Gene


class Individual:

    def __init__(self, chromosome=[]):
        self.chromosome = chromosome

    @staticmethod
    def init(cities, distances):
        Individual.cities = cities
        Individual.distances = distances
        Individual.indexes = dict(zip(cities, range(len(cities))))

    def fitness(self):
        distance = self.chromosome[0].distance(Gene.init_gene) + self.chromosome[-1].distance(Gene.init_gene)
        for i in range(len(self.chromosome) - 1):
            distance += self.chromosome[i].distance(self.chromosome[i+1])
        return distance

    def __str__(self):
        cities = []
        for gene in self.chromosome:
            cities.append(gene.__str__())
        return str(cities)+', fitness : '+str(self.fitness())


