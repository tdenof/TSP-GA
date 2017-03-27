import math


class Gene:

    init_gene = None

    def __init__(self, name=None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Gene):
            raise NotImplementedError
        return self.name == other.name

    @staticmethod
    def init(gene):
        Gene.init_gene = gene

    def distance(self, gene):
        distance = math.sqrt((self.x-gene.x)**2 + (self.y-gene.y)**2)
        return distance

    def __str__(self):
        return self.name
