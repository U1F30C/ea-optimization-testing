import Coins
import GeneticAlgorithm

def main():
    coins =  [ 1, 20,  5,  1,  2,  5,  5,  1,  5,  2,  2,  1, 10,  5, 10,  5, 20, 20, 20,  5,  1,  1, 20, 20,  1, 10,  2, 10,  5,  2, 10,  1, 20,  1, 20, 10,  5,  5, 20,  2, 10,  1,  2,  5, 10, 20, 10,  2,  5,  5, 20, 1,  1,  5, 10, 10, 10,  1,  5,  2,  1,  2, 10, 20,  2, 10, 10, 20, 5, 10,  1,  2,  1,  5, 20,  2,  5,  1,  5, 10,  2,  5, 10,  2,  1, 1,  1, 10, 20, 10, 20,  2,  2, 10, 20, 10,  1,  1,  5,  2]
    coins_problem = Coins.Coins(coins)
    allels = len(coins)
    population_size = 32
    generations = 200000
    mutation_rate = 0.1
    ag = GeneticAlgorithm.GeneticAlgorithm(population_size, allels, generations, mutation_rate, coins_problem)
    ag.run()

if __name__ == '__main__':
    main()
