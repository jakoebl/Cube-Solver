import move_tables as m

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


def gen_lookup():
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


lookup_moves = [[], [0], [1], [2], [3], [4], [5]]
lookup_string = ['uuuuuuuuffffffffllllllllbbbbbbbbrrrrrrrrdddddddd', "uuuuuuuubbbfffffrrrlllllfffbbbbblllrrrrrdddddddd", "uuuuddduffffffffllrrrlllbbbbbbbblrrrrrlluuuddddd", "duuuuuddbfffffbbllllllllbbfffbbbrrrrrrrruddddduu", "ddduuuuuffffffffrlllllrrbbbbbbbbrrlllrrrdddduuud", "uuddduuuffbbbfffllllllllfbbbbbffrrrrrrrrdduuuddd", "uuuuuuuuffffbbbfllllrrrlbbbbfffbrrrrlllrdddddddd"]
gen_lookup()