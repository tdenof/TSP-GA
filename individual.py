import warnings
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

    def plot_cities(self):
        x = [Gene.init_gene.x]
        y = [Gene.init_gene.y]

        for gene in self.chromosome:
            x.append(gene.x)
            y.append(gene.y)
            plt.annotate(gene.name, xy=(gene.x, gene.y), xytext=(5, 5), textcoords='offset points')

        plt.plot(x, y, 'co')

        # Ignore matplotlib warnings related to GUI
        warnings.filterwarnings("ignore", ".*GUI.*")

    def plot_paths(self, iteration, block=False):

        x = [Gene.init_gene.x]
        y = [Gene.init_gene.y]

        for gene in self.chromosome:
            x.append(gene.x)
            y.append(gene.y)

        n = len(x)
        for coord in range(len(x)):
            plt.arrow(x[coord], y[coord], (x[(coord+1) % n] - x[coord]), (y[(coord+1) % n] - y[coord]), color='r',
                      length_includes_head=True, head_width=0, width=0.001)

        plt.suptitle('Iteration : '+str(iteration)+' - Fitness : '+str(self.fitness()), fontsize=12)

        plt.show(block)
        plt.pause(0.1)
        ax = plt.gca()
        del ax.artists[:]

    def __str__(self):
        cities = []
        for gene in self.chromosome:
            cities.append(gene.__str__())
        return str(cities)+', fitness : '+str(self.fitness())


