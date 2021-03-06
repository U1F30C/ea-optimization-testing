import sphere
import rastrigin
import quartic
import rosenbrock
import GeneticAlgorithm
import numpy as np
import matplotlib.pyplot as plt

def zip_average(sets):
    result = np.repeat(0.0, len(sets[0]))
    for set in sets:
        for i in range(len(set)):
            result[i] += set[i]
    # print(result)
    for i in range(result.size):
        result[i] = -result[i] / len(sets)
    return result

zip_average([[1.5, 2], [5, 7], [4.0,6]])


def main():
    sphere_problem = sphere.Sphere()
    rastrigin_problem = rastrigin.Rastrigin()
    quartic_problem = quartic.Quartic()
    rosenbrock_problem = rosenbrock.Rosenbrock()
    # allels = 2
    population_size = 16
    generations = 2000
    mutation_rate = 0.1
    for allels in [2, 4, 8]:
        raw_sets = []
        for i in range(5):
            ag = GeneticAlgorithm.GeneticAlgorithm(population_size, allels, generations, mutation_rate, rastrigin_problem)
            
            raw_sets.append(ag.run())
        print(zip_average(raw_sets), allels)
        plt.plot(range(100, generations+100, 100), zip_average(raw_sets), label = str(allels))
    # plt.legend(['2', '4', '8'])
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()