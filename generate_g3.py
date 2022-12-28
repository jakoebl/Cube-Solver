import generate_8C4
# UBL cycle is 1, S slice is 1, BL and BR are 1
# corners first, standard order, then edges, U layer, then D layer, then E slice
R2_coord = (0, 5, 6, 3, 4, 1, 2, 7, 8, 13, 10, 11, 12, 9, 14, 15, 19, 17, 18, 16)

F2_coord = (0, 1, 4, 5, 2, 3, 6, 7, 8, 9, 12, 11, 10, 13, 14, 15, 17, 16, 18, 19)

U_coord = (3, 0, 1, 2, 4, 5, 6, 7, 11, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19)
U2_coord = (2, 3, 0, 1, 4, 5, 6, 7, 10, 11, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19)
Up_coord = (1, 2, 3, 0, 4, 5, 6, 7, 9, 10, 11, 8, 12, 13, 14, 15, 16, 17, 18, 19)

L2_coord = (4, 1, 2, 7, 0, 5, 6, 3, 8, 9, 10, 15, 12, 13, 14, 11, 16, 18, 17, 19)

B2_coord = (6, 7, 2, 3, 4, 5, 0, 1, 14, 9, 10, 11, 12, 13, 8, 15, 16, 17, 19, 18)

D_coord = (0, 1, 2, 3, 7, 4,  5, 6, 8, 9, 10, 11, 15, 12, 13, 14, 16, 17, 18, 19)
D2_coord = (0, 1, 2, 3, 6, 7, 4, 5, 8, 9, 10, 11, 14, 15, 12, 13, 16, 17, 18, 19)
Dp_coord = (0, 1, 2, 3, 5, 6, 7, 4, 8, 9, 10, 11, 13, 14, 15, 12, 16, 17, 18, 19)

moves = [U_coord, Up_coord, U2_coord, F2_coord, L2_coord,
         B2_coord, R2_coord, D_coord, Dp_coord, D2_coord]


def move(string, move):  # coordinate int
    result = ""
    for element in move:
        result += string[element]
    return result


def coordinate_4C2(string):
    lookup_4C2 = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}]
    return lookup_4C2.index({int(string[1]), int(string[0])})


def coordinate(string):
    result = generate_8C4.lookup.index(string[0] + string[2] + string[4] + string[6] + string[1] + string[3] + string[5] + string[7])
    result += 70 * generate_8C4.lookup.index(string[8] + string[10] + string[12] + string[14] + string[9] + string[11] + string[13] + string[15])
    result += 70 ** 2 * coordinate_4C2(string[16] + string[17])
    return result


def get_moves(string):
    result = list()
    for element in moves:
        result.append(move(string, element))
    return tuple(result)


def is_new(pos, distribution):
    for depth in distribution:
        if pos in depth:
            return False
    return True


def gen_empty_lookup():
    for num in range(29400):
        lookup.append([])
    for element in set(get_moves("01010101010101010123")):
        lookup[coordinate(element)] = [get_moves("01010101010101010123").index(element)]
    lookup[0] = ["solved"]

def gen_lookup():
    dist = [{"01010101010101010123"}, {'01010101010101013120', '01010101010101010132', '01010101010101010213', '01010101010101011023', '10100101101001010123', '01011010010110100123'}]
    gen_empty_lookup()
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1]))  # Shows distribution
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if not lookup[coordinate(subpos)] and is_new(subpos, dist):
                    dist[-1].add(subpos)
                    temp = []
                    for index in range(len(lookup[coordinate(pos)])):
                        temp.append(lookup[coordinate(pos)][index])
                    temp.append(get_moves(pos).index(subpos))
                    lookup[coordinate(subpos)] = temp
    for element in dist:
        if "01010101010101010123" in element:
            print("uh oh")


def write_lookup(file):
    gen_lookup()
    table_g3 = open(file, "w")
    for lists in lookup:
        for element in lists:
            table_g3.write(str(element))
            table_g3.write(" ")
        table_g3.write("\n")
    table_g3.close()


lookup = []
