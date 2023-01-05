# 1 means flipped edge
# in str notation, start at d1 from the left of the string
# order is d5 d3 d1 b5 b3 f5 f3 u7 u5 u3 u1

# moves affect edges
# 100 means flipping the edge
# otherwise this is perm of edges
R = (0, 4, 2, 3, 9, 5, 6, 1, 8, 7, 10, 11)
R2 = (0, 9, 2, 3, 7, 5, 6, 4, 8, 1, 10, 11)
Rp = (0, 7, 2, 3, 1, 5, 6, 9, 8, 4, 10, 11)

F = (0, 1, 105, 3, 102, 108, 6, 7, 104, 9, 10, 11)
F2 = (0, 1, 8, 3, 5, 4, 6, 7, 2, 9, 10, 11)
Fp = (0, 1, 104, 3, 108, 102, 6, 7, 105, 9, 10, 11)

U = (3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11)
U2 = (2, 3, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11)
Up = (1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11)

L = (0, 1, 2, 6, 4, 3, 11, 7, 8, 9, 10, 5)
L2 = (0, 1, 2, 11, 4, 6, 5, 7, 8, 9, 10, 3)
Lp = (0, 1, 2, 5, 4, 11, 3, 7, 8, 9, 10, 6)

B = (107, 1, 2, 3, 4, 5, 100, 110, 8, 9, 106, 11)
B2 = (10, 1, 2, 3, 4, 5, 7, 6, 8, 9, 0, 11)
Bp = (106, 1, 2, 3, 4, 5, 110, 100, 8, 9, 107, 11)

D = (0, 1, 2, 3, 4, 5, 6, 7, 11, 8, 9, 10)
D2 = (0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 8, 9)
Dp = (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8)

moves = [U, Up, U2, F, Fp, F2, L, Lp, L2, B, Bp, B2, R, Rp, R2, D, Dp, D2]


# takes coord and flip_move
# converts coordinate to string
# applies move to string
# converts string back to coordinate
def coordinate_move(coordinate_int, move):  # coordinate int
    result = ""
    string = string_from_coordinate(coordinate_int)
    for element in move:
        if element < 12:
            result += string[element]
        else:
            if string[element % 100] == "1":
                result += "0"
            else:
                result += "1"
    return coordinate(result)


# convert int to 12 bit binary number stored in a string for use in coordinate level moves
def string_from_coordinate(integer):
    result = ""
    exponent = 10
    while exponent > -1:
        if integer >= 2 ** exponent:
            integer -= 2 ** exponent
            result += "1"
        else:
            result += "0"
        exponent -= 1
    if result.count("1") % 2 == 1:
        result += "1"
    else:
        result += "0"
    return result


# converts back to coordinate from 12 bit binary number in string
def coordinate(string):
    exponent = 10
    result = 0
    for bit in string:
        if bit == "1":
            result += 2 ** exponent
        exponent -= 1
        if exponent == -1:
            break
    return result


def get_moves(coordinate):
    result = []
    for move in moves:
        result.append(coordinate_move(coordinate, move))
    return result


def gen_empty_lookup():
    result = []
    for index in range(2048):
        result.append([])
    result[356] = [3]
    result[1049] = [9]
    return result


def gen_lookup():
    dist = [{0}, {1049, 356}]
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1]))  # Shows distribution
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if subpos not in dist[-3] and subpos not in dist[-2] and subpos not in dist[-1]:
                    dist[-1].add(subpos)
                    lookup[subpos] = lookup[pos] + [get_moves(pos).index(subpos)]


def write_lookup(file):
    table_g1 = open(file, "w")
    gen_lookup()
    for lists in lookup:
        for move in lists:
            table_g1.write(str(move))
            table_g1.write(" ")
        table_g1.write("\n")
    table_g1.close()


lookup = []
# lookup = gen_empty_lookup()
# gen_lookup()
