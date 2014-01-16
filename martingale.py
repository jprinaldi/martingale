from roulette import Roulette
from gambler import Gambler

def mean(list):
    return sum(list)/len(list)

def martingale(initialWealth, betAmount):
    roulette = Roulette()
    gambler = Gambler(initialWealth)

    while gambler.getWealth() >= betAmount:
        winnings = roulette.betColor(betAmount)
        gambler.decrementWealth(betAmount)
        gambler.incrementWealth(winnings)
        if winnings > 0:
            break
        betAmount *= 2

    return gambler.getWealth()

if __name__ == "__main__":
    # Output mean winnings when using the martingale betting strategy
    # Assume minimum bet is 1.0 and maximum bet is 200.0
    # initialWealth = 255.0 guarantees non-negative wealth
    initialWealth = 255.0
    initialBet = 1.0
    wealths = []
    numTrials = 10000

    for trial in range(numTrials):
        wealth = martingale(initialWealth, initialBet)
        wealths.append(wealth)

    meanWinnings = mean(wealths) - initialWealth
    print meanWinnings