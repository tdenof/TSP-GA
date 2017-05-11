import csv
import argparse
from individual import Individual
from population import Population
from gene import Gene

parser = argparse.ArgumentParser(description='Travel Salesman Problem with Genetic Algorithm.')
parser.add_argument('-s', '--size', type=int, default=None,
                    help='Population size, default is cities count.')
parser.add_argument('-i', '--iteration', type=int, default=100,
                    help='Iterations limit for GA, default is 100.')
parser.add_argument('--cp', metavar="Probability", type=float, default=0.9,
                    help='Crossover probability, default is 0.9.')
parser.add_argument('--mp', metavar="Probability", type=float, default=0.05,
                    help='Mutation probability, default is 0.05.')
parser.add_argument('-f', '--file', default='dataset.csv',
                    help='Dataset input file in csv format, if not given will look for the file \'dataset.csv\'.')
parser.add_argument('-p', '--frequency', type=int, default=10,
                    help='Plot frequency, default is 10 iterations, a negative value will prevent intermediate plot.'
                         ' Keep in mind that plot cost time and resources.')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Print detailed information about road search.')
args = parser.parse_args()
cmdopt = vars(args)
size = cmdopt.get('size')
dsfile = cmdopt.get('file')
max_iterations = cmdopt.get('iteration')
cp = cmdopt.get('cp')
mp = cmdopt.get('mp')
frequency = cmdopt.get('frequency')
verbose = cmdopt.get('verbose')

chromosome = []
with open(dsfile) as datasetFile:
    dataset = csv.reader(datasetFile, delimiter=',')
    line = dataset.next()
    init_city = Gene(line[0], int(line[1]), int(line[2]))
    Gene.init(init_city)
    for row in dataset:
        chromosome.append(Gene(row[0], int(row[1]), int(row[2])))

if not size:
    size = len(chromosome)+1

print "Starting Genetic Algorithm with the following parameters :"
print "Genes (cities) count : ", len(chromosome)+1
print "Population size : ", size
print "Crossover probability : ", cp
print "Mutation probability : ", mp
print "Iterations limit : ", max_iterations

individual = Individual(chromosome)
individual.plot_cities()

population = Population(individual, size)
Population.init_probabilities(cp, mp)
if verbose:
    print 'Initial Population :'
    print population

elite = population.fittest()

if verbose:
    print "Elite is : ", elite
elite.plot_paths(0)

best_individual = elite
best_iteration = 0
j = 0
for iteration in range(0, max_iterations+1):
    population.selection()

    population.crossover()

    population.mutation()

    elite = population.fittest()
    if best_individual.fitness() > elite.fitness():
        best_individual = elite
        best_iteration = iteration

    if verbose:
        print "Iteration : ", iteration, ", Fitness : ", elite.fitness()

    if j == frequency:
        elite.plot_paths(iteration)
        j = 0
    j += 1

if verbose:
    print "Final population : "
    print population

print "Elite found on iteration : ", best_iteration
print "Elite is : ", best_individual
best_individual.plot_paths(best_iteration, True)
