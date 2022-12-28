
test = open("lookup_g2", "r")

lines = test.readlines()
test.close()

dist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

move_started = False
for sequence in lines:
    count = 0
    for element in sequence:
        if element != " " and element != "\n" and not move_started:
            count += 1
            move_started = True
        else:
            move_started = False
    dist[count] += 1


print(dist)

