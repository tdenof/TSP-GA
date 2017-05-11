# TSP-GA
Solve the travel salesman problem using genetical algorithm

The code is compatible with ***Python 2.7***.  
```
usage: tsp.py [-h] [-s SIZE] [-i ITERATION] [--cp Probability]
              [--mp Probability] [-f FILE] [-p FREQUENCY] [-v]

Travel Salesman Problem with Genetic Algorithm.

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Population size, default is cities count.
  -i ITERATION, --iteration ITERATION
                        Iterations limit for GA, default is 100.
  --cp Probability      Crossover probability, default is 0.9.
  --mp Probability      Mutation probability, default is 0.05.
  -f FILE, --file FILE  Dataset input file in csv format, if not given will
                        look for the file 'dataset.csv'.
  -p FREQUENCY, --frequency FREQUENCY
                        Plot frequency, default is 10 iterations, a negative
                        value will prevent intermediate plot. Keep in mind
                        that plot cost time and resources.
  -v, --verbose         Print detailed information about road search.
```
