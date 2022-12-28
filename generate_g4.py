import math
import g4_corners
import g4_edges
import move_tables as m
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


def move(string, move):
    result = ""
    for element in move:
        result += string[element]
    return result


def get_moves(string):
    result = []
    for element in m.moves_g4:
        result.append(move(string, element))
    return result


def is_new(pos, distribution):
    for depth in distribution:
        if pos in depth:
            return False
    return True


def gen_lookup_g4():
    dist = [{'uuuuuuuuffffffffllllllllbbbbbbbbrrrrrrrrdddddddd'}, {"uuuuuuuubbbfffffrrrlllllfffbbbbblllrrrrrdddddddd", "uuuuddduffffffffllrrrlllbbbbbbbblrrrrrlluuuddddd", "duuuuuddbfffffbbllllllllbbfffbbbrrrrrrrruddddduu", "ddduuuuuffffffffrlllllrrbbbbbbbbrrlllrrrdddduuud", "uuddduuuffbbbfffllllllllfbbbbbffrrrrrrrrdduuuddd", "uuuuuuuuffffbbbfllllrrrlbbbbfffbrrrrlllrdddddddd"}]
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1]))  # Shows distribution
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if is_new(subpos, dist):
                    dist[-1].add(subpos)
                    lookup_string.append(subpos)
                    lookup_moves.append(lookup_moves[lookup_string.index(pos)] + [get_moves(pos).index(subpos)])


def write_lookup(file_moves, file_strings):
    gen_lookup_g4()

    moves_g4 = open(file_moves, "w")
    strings_g4 = open(file_strings, "w")

    for lists in lookup_moves:
        for element in lists:
            moves_g4.write(str(element))
            moves_g4.write(" ")
        moves_g4.write("\n")

    for string in lookup_string:
        strings_g4.write(string)
        strings_g4.write("\n")

    moves_g4.close()
    strings_g4.close()


lookup_g4 = []
lookup_moves = [[], [0], [1], [2], [3], [4], [5]]
lookup_string = ['uuuuuuuuffffffffllllllllbbbbbbbbrrrrrrrrdddddddd', "uuuuuuuubbbfffffrrrlllllfffbbbbblllrrrrrdddddddd", "uuuuddduffffffffllrrrlllbbbbbbbblrrrrrlluuuddddd", "duuuuuddbfffffbbllllllllbbfffbbbrrrrrrrruddddduu", "ddduuuuuffffffffrlllllrrbbbbbbbbrrlllrrrdddduuud", "uuddduuuffbbbfffllllllllfbbbbbffrrrrrrrrdduuuddd", "uuuuuuuuffffbbbfllllrrrlbbbbfffbrrrrlllrdddddddd"]
write_lookup("moves_g4", "strings_g4")
