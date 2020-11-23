class Coins:
    def __init__(self, coins):
        self._coins = coins

    def f(self, chromosome):
        amount = 0
        adjacentCount = 0
        takenCoins = 0
        for i in range(len(chromosome)):
            if chromosome[i]:
                amount = amount + self._coins[i]
                takenCoins += 1
                if (i < len(chromosome) - 1) and chromosome[i + 1]:
                    adjacentCount += 1
        if adjacentCount == 0:
            return amount
        else:
            return -adjacentCount
