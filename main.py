import generate_g1 as g1
import generate_g2 as g2
import generate_g3 as g3
import generate_g4 as g4
import move_tables as move
import facelet_moves as m
import facelet_manipulation_stuff as p
identity = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
            'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f',
            'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l',
            'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
            'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
            'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']


def corners(*perms):
    perm = m.mult(*perms)
    result = []
    i = 0
    while i < 48:
        result.append(perm[i])
        i += 2
    return result


def edges(*perms):
    perm = m.mult(*perms)
    result = []
    i = 1
    while i < 48:
        result.append(perm[i])
        i += 2
    return result


def g2_corner_coordinate(*perms):
    perm = corners(m.mult(*perms))
    coordinate = 0
    exp = 1
    for element in ['u1', 'u3', 'u5', 'u7', 'd1', 'd3', 'd5']:
        if perm.index(element) in [0, 1, 2, 3, 20, 21, 22, 23]:
            exp *= 3
        elif perm.index(element) in [4, 6, 8, 10, 12, 14, 16, 18]:
            coordinate += exp
            exp *= 3
        else:
            coordinate += exp * 2
            exp *= 3
    return coordinate


def g1_coordinate(perm):
    result = ""
    for edge in p.edges(perm):
        if edge in p.edges_solved:
            result += "0"
        else:
            result += "1"
    return g1.coordinate(result)


def g2_coordinate(perm):
    result = ""
    for corner in p.corners(perm):
        if corner in p.corners_solved:
            result += "0"
        elif p.corner_rotation(corner) in p.corners(perm):
            result += "1"
        else:
            result += "2"
    transform = [0, 1, 2, 3, 8, 9, 10, 11, 4, 5, 6, 7]
    edges_rearranged = []
    for index in transform:
        edges_rearranged.append(p.edges(perm)[index])
    for edge in edges_rearranged:
        if edge in [('f', 'r'), ('f', 'l'), ('b', 'l'), ('b', 'r')] or p.flip(edge) in [('f', 'r'), ('f', 'l'), ('b', 'l'), ('b', 'r')]:
            result += "1"
        else:
            result += "0"
    return g2.coordinate(result)


def g3_coordinate(perm):
    result = ""
    for corner in p.corners(perm):
        if corner in [('u', 'l', 'b'), ('u', 'r', 'f'), ('d', 'l', 'f'), ('d', 'r', 'b')]:
            result += "0"
        else:
            result += "1"
    # order found in gen_g3
    transform = [0, 1, 2, 3, 8, 9, 10, 11, 4, 5, 6, 7]
    edges_transformed = []
    for index in transform:
        edges_transformed.append(p.edges(perm)[index])

    for edge in edges_transformed:
        if edge in [('u', 'r'), ('u', 'l'), ('d', 'r'), ('d', 'l')]:
            result += "1"
        elif edge in [('f', 'r'), ('f', 'l'), ('b', 'l'), ('b', 'r')]:
            result += str([('f', 'r'), ('f', 'l'), ('b', 'l'), ('b', 'r')].index(edge))
        else:
            result += "0"
    return g3.coordinate(result)


def g4_coordinate(perm):
    result = ""
    cycle1 = []
    cycle2 = []
    for index in [0, 2, 4, 6]:
        cycle1.append(p.corners(perm)[index])
        cycle2.append(p.corners(perm)[index + 1])
    cycle_m = []
    for index in [0, 2, 8, 10]:
        cycle_m.append(p.edges(perm)[index])
    cycle_s = []
    for index in [3, 1, 9, 11]:
        cycle_s.append(p.edges(perm)[index])
    cycle_e = []
    for index in [4, 5, 6, 7]:
        cycle_e.append(p.edges(perm)[index])
    for cycle in [cycle1, cycle2, cycle_e, cycle_s, cycle_m]:
        print(cycle)
        for piece in cycle:
            for lists in p.piece_index_g4:
                if piece in lists:
                    result += str(p.piece_index_g4.index(lists))
    print(g4.coordinate(result), result)
    return g4.coordinate(result)


# read all lines
g1_file = open("lookup_g1", "r")
g2_file = open("lookup_g2", "r")
g3_file = open("lookup_g3", "r")
g4_file = open("lookup_g4", "r")

g1_table = g1_file.readlines()
g2_table = g2_file.readlines()
g3_table = g3_file.readlines()
g4_table = g4_file.readlines()

g1_file.close()
g2_file.close()
g3_file.close()
g4_file.close()
move_list = []


def lookup_moves(table, coordinate):
    result = []
    move_curr = ""
    if coordinate == 0:
        return []
    if int(table[coordinate][0]) not in range(10):
        return []
    for index in range(int(len(table[coordinate])) - 1):
        if table[coordinate][index] != " ":
            move_curr += table[coordinate][index]
        else:
            result.append(int(move_curr))
            move_curr = ""
    return result


# input perm in facelet notation
input_perm = m.apply(move.D2, move.B2, move.F2, move.R2, move.U2, move.L2, move.U2, move.B2, move.L2, move.R2)
# solution is a list of ints
solution_g1 = move.invert(lookup_moves(g1_table, g1_coordinate(input_perm)))
if solution_g1:
    print(solution_g1)
# bring input  to g1
for move_index in solution_g1:
    input_perm = m.apply_single(input_perm, move.moves[move_index])


solution_g2 = move.invert(move.translate(lookup_moves(g2_table, g2_coordinate(input_perm)), move.moves_g2))
if solution_g2:
    print(solution_g2)

# bring input to g2:
for move_index in solution_g2:
    input_perm = m.apply_single(input_perm, move.moves[move_index])


solution_g3 = move.invert(move.translate(lookup_moves(g3_table, g3_coordinate(input_perm)), move.moves_g3))
if solution_g3:
    print(solution_g3)

# bring input to g3:
for move_index in solution_g3:
    input_perm = m.apply_single(input_perm, move.moves[move_index])

solution_g4 = move.invert(move.translate(lookup_moves(g4_table, g4_coordinate(input_perm)), move.moves_g4))
if solution_g4:
    print(solution_g4)
# bring input to g4:
for move_index in solution_g4:
    input_perm = m.apply_single(input_perm, move.moves[move_index])

# check if solution is correct
if not input_perm == move.identity:
    print("Something went wrong")

solution = solution_g1 + solution_g2 + solution_g3 + solution_g4
print(move.moves_string(solution))
print(lookup_moves(g4_table, 172573))
