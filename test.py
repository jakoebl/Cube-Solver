import random
import main
import move_tables as m
test_sample = 10000
result = 0
for _ in range(test_sample):
    scramble = m.apply(m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                       m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                       m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                       m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)],
                       m.moves[random.randint(0, 17)], m.moves[random.randint(0, 17)])
    result += len(main.solve(scramble))
    for element in main.solve(scramble):
        if (element + 1) % 3 == 0:
            result -= 1
print(result / test_sample)
