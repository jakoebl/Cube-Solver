import random
import main
import facelet_moves as move
import move_tables as m

result = 0
for _ in range(10000):
    for i in range(20):
        scramble = move.apply(m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                              m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                              m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                              m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)])
    result += main.solve(scramble)
print(result / 1000)
