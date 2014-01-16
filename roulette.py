import random

class Roulette:
    def __init__(self):
        self.numbers = range(37)

    def spin(self):
        return random.choice(self.numbers)

    def betColor(self, betAmount):
        number = self.spin()
        if number == 0:
            return 0
        elif number % 2 == 0:
            return 2*betAmount
        else:
            return 0