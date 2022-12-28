import math
import g4_corners
import g4_edges
# order of cycles: UBL UBR E S M
R2 = (0, 3, 2, 1, 6, 5, 4, 7, 11, 9, 10, 8, 12, 14, 13, 15, 16, 17, 18, 19)

F2 = (0, 2, 1, 3, 4, 6, 5, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 18, 17, 19)

U2 = (1, 0, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19)

L2 = (2, 1, 0, 3, 4, 7, 6, 5, 8, 10, 9, 11, 15, 13, 14, 12, 16, 17, 18, 19)

B2 = (3, 1, 2, 0, 7, 5, 6, 4, 8, 9, 11, 10, 12, 13, 14, 15, 19, 17, 18, 16)

D2 = (0, 1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 15, 14, 16, 17, 19, 18)

moves = (U2, F2, L2, B2, R2, D2)

perm_lookup = ['0123', '1023', '0213', '2013', '1203', '2103', '0132', '1032', '0312', '3012', '1302', '3102',
               '0231', '2031', '0321', '3021', '2301', '3201', '1230', '2130', '1320', '3120', '2310', '3210']


def corner_coordinate_from_string(string):
    return g4_corners.lookup.index(string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7])


def edge_coordinate_from_string(string):
    result = g4_edges.lookup.index(string[12] + string[13] + string[14] + string[15] + string[16] + string[17])
    result += 288 * perm_lookup.index(string[8] + string[9] + string[10] + string[11])
    return result


def coordinate(string):
    return corner_coordinate_from_string(string) + 96 * edge_coordinate_from_string(string)


def move(string, move):
    result = ""
    for element in move:
        result += string[element]
    return result


def get_moves(string):
    result = []
    for element in moves:
        result.append(move(string, element))
    return result


def is_new(pos, distribution):
    for depth in distribution:
        if pos in depth:
            return False
    return True


def gen_lookup_g4():
    dist = [{'01230123012301230123'}, {'10231023012310231023', '02130213102301230213', '21030321021331200123', '31203120013201233120', '03212103312002130123', '01320132012301320132'}]
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1]))  # Shows distribution
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if is_new(subpos, dist):
                    dist[-1].add(subpos)
                    temp = []
                    for index in range(len(lookup_g4[coordinate(pos)])):
                        temp.append(lookup_g4[coordinate(pos)][index])
                    temp.append(get_moves(pos).index(subpos))
                    lookup_g4[coordinate(subpos)] = temp


def write_lookup(file):
    for number in range(663552):
        lookup_g4.append("")
    for mov in get_moves("01230123012301230123"):
        lookup_g4[coordinate(mov)] = [get_moves("01230123012301230123").index(mov)]
    gen_lookup_g4()
    table_g4 = open(file, "w")
    for lists in lookup_g4:
        for element in lists:
            table_g4.write(str(element))
            table_g4.write(" ")
        table_g4.write("\n")
    table_g4.close()


lookup_g4 = []
print(coordinate("20312031013231200321"))
print(coordinate("02312013013230210312"))