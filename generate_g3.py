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


def get_coordinates(string):
    result = []
    for element in m.moves_g3:
        result.append(coordinate(move(string, element)))
        result.append(m.moves_g3.index(element))
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
    result = corner_parity(corners)
    result += 2 * generate_8C4.lookup.index(edge_string)
    result += 140 * int(corner_coord(string))
    return result


def gen_lookup():
    result = 0
    dist = [{'uuuuuuuuffffffffllllllllbbbbbbbbrrrrrrrrdddddddd'}, {'uuuuddduffffffffllrrrlllbbbbbbbblrrrrrlluuuddddd', 'uuddduuuffbbbfffllllllllfbbbbbffrrrrrrrrdduuuddd', 'ddduuuuuffffffffrlllllrrbbbbbbbbrrlllrrrdddduuud', 'uuuuuuuubbbfffffrrrlllllfffbbbbblllrrrrrdddddddd', 'uuuuuuuuffffbbbfllllrrrlbbbbfffbrrrrlllrdddddddd', 'uuuuuuuulllfffffbbblllllrrrbbbbbfffrrrrrdddddddd', 'duuuuuddbfffffbbllllllllbbfffbbbrrrrrrrruddddduu'}
]
    coordinates = {4524941440, 141725260, 4494449440, 1445249440, 4524941447, 4524941493}
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1])) # Shows distribution
        result += len(dist[-1])
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if coordinate(subpos) not in coordinates:
                    dist[-1].add(subpos)
                    coordinates.add(coordinate(subpos))
                    lookup_moves.append(lookup_moves[lookup_coordinates.index(coordinate(pos))] + [get_moves(pos).index(subpos)])
                    lookup_coordinates.append(coordinate(subpos))
    print(result)
    print(len(dist) - 2)


def corner_coord(string):
    corners = p.corners(string)
    corner_list = [0, 0, 1, 1, 2, 2, 3, 3]
    for index in range(8):
        corner_list[index] = p.corners_g3.index(corners[index]) % 4
    ordered_list = []
    for i in range(4):
        ordered_list.append(corner_list.index(i))
    ordered_list.sort()
    for num in range(4):
        ordered_list[num] = corner_list[ordered_list[num]]
    for n in range(8):
        corner_list[n] = ordered_list.index(corner_list[n])
    result = ""
    base = 1
    for element in corner_list:
        result += str(element)
        base *= 10
    return result


lookup_moves = [[], [0], [1]]
lookup_coordinates = [4524941440, 141725260, 4524941440, 4494449440, 1445249440, 4524941447, 4524941493]


gen_lookup()
