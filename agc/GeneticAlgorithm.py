import copy
import numpy as np
import math

class Individual:
    def __init__(self, allels, chromosome):
        self._allels = allels
        self._chromosome = chromosome
        self._fitness = 0

class GeneticAlgorithm:
    def __init__(self, population_size, allels, generations, mutation_rate, problem):
        self._population_size = population_size
        self._allels = allels
        self._generations = generations
        self._mutation_rate = mutation_rate
        self._problem = problem
        self.population = np.array([])

    def run(self):
        self.pupulate()
        self._most_fit = self.population[0]
        generation = 1
        history = []
        while generation <= self._generations:
            self.evaluatePopulation(generation)
            children = np.array([])
            while len(children) < len(self.population):
                parent1 = self.selectRandom()
                parent2 = self.selectRandom()
                while parent1 == parent2:
                    parent2 = self.selectRandom()
                h1, h2 = self.breed(self.population[parent1], self.population[parent2])
                children = np.append(children, [h1])
                children = np.append(children, [h2])
            self.mutate(children)
            self.population = np.copy(children)
            self.population[np.random.randint(len(self.population))] = copy.deepcopy(self._most_fit)
                
            if generation % 100 == 0: 
                history.append(self._most_fit._fitness)

            generation += 1
        return history

    def pupulate(self):
        for i in range(self._population_size):
            values = np.random.rand(self._allels)
            chromosome = self._problem.MIN_VALUE +  values * self._problem.RANGE
            individuo = Individual(self._allels, chromosome)
            self.population = np.append(self.population, [individuo])

    def evaluatePopulation(self, generation):
        for i in self.population:
            i._fitness = self._problem.f(i._chromosome)
            if i._fitness > self._most_fit._fitness:
                self._most_fit = copy.deepcopy(i)
                # print("Generación: ", generation, 'Mejor Histórico: ', self._most_fit._chromosome, self._most_fit._fitness)
        self.population = sorted(self.population, key= lambda i: i._fitness)

    def selectRandom(self):
        upper_limit = len(self.population)
        lower_limit = math.floor(upper_limit / 2)

        return np.random.randint(lower_limit, upper_limit)

    def breed(self, i1, i2):
        h1 = copy.deepcopy(i1)
        h2 = copy.deepcopy(i2)

        s = self._allels - 1
        breed_point = np.random.randint(s) + 1
        h1._chromosome[breed_point:], h2._chromosome[breed_point:] = h2._chromosome[breed_point:], h1._chromosome[breed_point:]
        return h1, h2

    def mutate(self, children):
        for child in children:
            for bit in range(len(child._chromosome)):
                if np.random.rand() < self._mutation_rate:
                    child._chromosome[bit] = self._problem.MIN_VALUE + np.random.rand() * self._problem.RANGE
