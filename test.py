import random
import main
import facelet_moves as move
import move_tables as m
test_sample = 500000
result = 0
for _ in range(test_sample):
    scramble = move.apply(m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                          m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                          m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                          m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                          m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)])
    result += len(main.solve(scramble))
print(result / test_sample)
