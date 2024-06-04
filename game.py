from numpy.random import randint


class Game:
    def __init__(self, player1, player2, round):
        self.player1 = player1
        self.player2 = player2
        self.round = round

    def __playRound(self):
        self.player1.boost(randint(-25, 25))
        self.player2.boost(randint(-25, 25))

        return f"[({self.player1.getEnergy()},{self.player2.getEnergy()})]"

    def winner(self):
        if self.player1.getEnergy() > self.player2.getEnergy():
            winner = self.player1
        else:
            winner = self.player2
        return winner

    def play(self):

        for i in range(self.round):
            j = i +1
            print(f"Round {j:1}: {self.__playRound()}")
