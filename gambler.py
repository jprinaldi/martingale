class Gambler:
    def __init__(self, initialWealth):
        self.wealth = initialWealth

    def getWealth(self):
        return self.wealth

    def incrementWealth(self, amount):
        self.wealth += amount

    def decrementWealth(self, amount):
        self.wealth -= amount