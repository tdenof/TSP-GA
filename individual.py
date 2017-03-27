from gene import Gene
from matplotlib import pyplot as plt


class Individual:

    def __init__(self, chromosome=[]):
        self.chromosome = chromosome
        self.quotient = 0
        self.remainder = 0

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

    def set_quorem(self, mean):
        self.quotient = int(mean/self.fitness())
        self.remainder = mean/self.fitness() - self.quotient

    def plot(self, iteration, block=False):
        x = [Gene.init_gene.x]
        y = [Gene.init_gene.y]

        for gene in self.chromosome:
            x.append(gene.x)
            y.append(gene.y)

        plt.plot(x, y, 'co')

        for coord in range(len(x)-1):
            plt.arrow(x[coord], y[coord], (x[coord+1] - x[coord]), (y[coord+1] - y[coord]), color='r',
                      length_includes_head=True, head_width=0, width=0.001)
        plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width=0, color='r', length_includes_head=True,
                  width=0.001)
        plt.suptitle('Iteration : '+str(iteration)+' - Fitness : '+str(self.fitness()), fontsize=12)

        plt.show(block)
        plt.pause(0.1)
        if not block:
            plt.clf()

    def __str__(self):
        cities = []
        for gene in self.chromosome:
            cities.append(gene.__str__())
        return str(cities)+', fitness : '+str(self.fitness())


