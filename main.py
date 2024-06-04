from jugador import Player
from game import Game

p1 = Player(1, "a")
p2 = Player(2, "b")

g1 = Game(p1, p2, 3)

print(p1.toString())
print(p2.toString())

g1.play()

print(g1.winner().toString())

p1.boost(-100)

print(p1.toString())

p1.boost(200)

print(p1.toString())

print(g1.winner().toString())


