import sphere
import rastrigin
import quartic
import rosenbrock
import GeneticAlgorithm

def main():
    sphere_problem = sphere.Sphere()
    rastrigin_problem = rastrigin.Rastrigin()
    quartic_problem = quartic.Quartic()
    rosenbrock_problem = rosenbrock.Rosenbrock()
    allels = 2
    population_size = 32
    generations = 200000
    mutation_rate = 0.1
    ag = GeneticAlgorithm.GeneticAlgorithm(population_size, allels, generations, mutation_rate, rosenbrock_problem)
    ag.run()

if __name__ == '__main__':
    main()
