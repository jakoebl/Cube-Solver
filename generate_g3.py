import move_tables as m
import generate_8C4
import facelet_manipulation_stuff as p


def move(string, move):
    result = ""
    for element in move:
        result += string[element]
    return result


def get_moves(string):
    result = []
    for element in m.moves_g3:
        result.append(move(string, element))

    return result


def is_new(pos, distribution):
    for depth in distribution:
        if pos in depth:
            return False
    return True


def corner_parity(corners):
    result = 0
    for i in range(0, 7):
        for j in range(i + 1, 8):
            result ^= bool(p.corners_solved.index(corners[i]) > p.corners_solved.index(corners[j]))
    return result


def coordinate(string):
    edges = p.edges(string)
    edge_string = ""
    for edge in edges:
        if edge in p.m_slice:
            edge_string += "0"
        elif edge in p.s_slice:
            edge_string += "1"

    corners = p.corners(string)
    corner_string = ""
    for corner in corners:
        corner_string += str(p.corners_g3.index(corner) % 4)

    result = corner_parity(corners)
    result += 2 * generate_8C4.lookup.index(edge_string)
    result += 140 * int(corner_string)
    return result


def gen_lookup():
    result = 0
    dist = [{'uuuuuuuuffffffffllllllllbbbbbbbbrrrrrrrrdddddddd'}, {'duuuuuddbfffffbbllllllllbbfffbbbrrrrrrrruddddduu', 'uuddduuuffbbbfffllllllllfbbbbbffrrrrrrrrdduuuddd', 'uuuuddduffffffffllrrrlllbbbbbbbblrrrrrlluuuddddd', 'uuuuuuuubbbfffffrrrlllllfffbbbbblllrrrrrdddddddd', 'uuuuuuuulllfffffbbblllllrrrbbbbbfffrrrrrdddddddd', 'uuuuuuuuffffrrrfllllffflbbbblllbrrrrbbbrdddddddd', 'ddduuuuuffffffffrlllllrrbbbbbbbbrrlllrrrdddduuud'}]
    coordinates = {141725260, 449694460, 2944244980, 172217260, 141852527, 1414325313, 3221722180, 141852527}
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1])) # Shows distribution
        result += len(dist[-1])
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if coordinate(subpos) not in coordinates:
                    dist[-1].add(subpos)
                    coordinates.add(coordinate(subpos))
                    lookup_moves.append(lookup_moves[lookup_strings.index(pos)] + [get_moves(pos).index(subpos)])
    print(result)
    print(len(dist) - 2)


lookup_moves = []
lookup_strings = []
gen_lookup()

