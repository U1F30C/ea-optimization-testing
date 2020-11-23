import copy
import numpy as np
import math

class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.best_known_position = copy.deepcopy(self.position)

class ParticleSwarmAlgorithm:
    def __init__(self, population_size, n_dimentions, generations, learning_rate, problem):
        self._population_size = population_size
        self._n_dimentions = n_dimentions
        self._generations = generations
        self._problem = problem
        self.learning_rate = learning_rate
        self.population = np.array([])

    def run(self):
        self.pupulate()
        generation = 1
        history = []
        while generation <= self._generations:

            for particle in self.population:
                rp = np.random.rand()
                rg = np.random.rand()
                w = 1
                phi_p = 1
                phi_g = 1
                particle.velocity = w * particle.velocity + phi_p * rp * (particle.best_known_position - particle.position) + phi_g * rg * (self.best_known_position - particle.position)
                particle.position = particle.position + particle.velocity * self.learning_rate

                if(self._problem.f(particle.position) > self._problem.f(particle.best_known_position)):
                    particle.best_known_position = particle.position

                    if(self._problem.f(particle.best_known_position) > self._problem.f(self.best_known_position)):
                        self.best_known_position = particle.best_known_position
            

            if generation % 100 == 0: 
                history.append(self._problem.f(self.best_known_position))

            generation += 1
        return history

    def pupulate(self):
        self.best_known_position =  self._problem.MIN_VALUE +  np.random.rand(self._n_dimentions) * self._problem.RANGE
        for i in range(self._population_size):
            position = self._problem.MIN_VALUE +  np.random.rand(self._n_dimentions) * self._problem.RANGE
            if(self._problem.f(position) > self._problem.f(self.best_known_position)):
                self.best_known_position = position
            
            velocity = -self._problem.RANGE +  np.random.rand(self._n_dimentions) * 2 * self._problem.RANGE
            particle = Particle(position, velocity) 

            self.population = np.append(self.population, [particle])
