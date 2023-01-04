import generate_g1 as g1
import generate_g2 as g2
import move_tables as move
import facelet_moves as m
import facelet_manipulation_stuff as p


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
        elif p.corner_clockwise_rotation(corner) in p.corners_solved:
            result += "2"
        else:
            result += "1"
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


def g3_string(perm):
    result = ""
    for corner in p.corners(perm):
        result += str(p.corners_solved.index(corner))
    # order found in gen_g3
    transform = [0, 1, 2, 3, 8, 9, 10, 11, 4, 5, 6, 7]
    edges_transformed = []
    for index in transform:
        edges_transformed.append(p.edges(perm)[index])

    for edge in edges_transformed:
        if edge in [('u', 'r'), ('u', 'l'), ('d', 'r'), ('d', 'l')]:
            result += "1"
        elif edge not in [('f', 'r'), ('f', 'l'), ('b', 'l'), ('b', 'r')]:
            result += "0"

    result += "xxxx"

    result += str(p.corner_parity(p.corners(perm)))

    result += "\n"
    return result


def g4_string(perm):
    result = ""
    for element in perm:
        result += element
    return result


# read all lines
g1_file = open("lookup_g1", "r")
g2_file = open("lookup_g2", "r")
moves_g3 = open("moves_g3", "r")
strings_g3 = open("strings_g3", "r")
moves_g4 = open("moves_g4", "r")
strings_g4 = open("strings_g4", "r")

g1_table = g1_file.readlines()
g2_table = g2_file.readlines()
g3_strings = strings_g3.readlines()
g3_moves = moves_g3.readlines()
g4_moves = moves_g4.readlines()
g4_strings_temp = strings_g4.readlines()
g4_strings = []

for line in g4_strings_temp:
    g4_strings.append(line.strip())

g1_file.close()
g2_file.close()
moves_g3.close()
strings_g3.close()
moves_g4.close()
strings_g4.close()

move_list = []


def lookup_moves(table, coordinate):
    result = []
    move_curr = ""
    if coordinate == 0:
        return []
    if "s" in table[coordinate]:
        return []
    for index in range(int(len(table[coordinate])) - 1):
        if table[coordinate][index] != " ":
            move_curr += table[coordinate][index]
        else:
            result.append(int(move_curr))
            move_curr = ""
    return result


def index_string(table, string):
    return table.index(string)


def solve(input_perm):
    # solution is a list of ints
    solution_g1 = []
    solution_g2 = []
    solution_g3 = []
    solution_g4 = []

    if g1_coordinate(input_perm) != 0:
        solution_g1 = move.invert(lookup_moves(g1_table, g1_coordinate(input_perm)))

        # bring input  to g1
        for move_index in solution_g1:
            input_perm = m.apply_single(input_perm, move.moves[move_index])

    if g2_coordinate(input_perm) != 0:
        solution_g2 = move.invert(move.translate(lookup_moves(g2_table, g2_coordinate(input_perm)), move.moves_g2))

        # bring input to g2:
        for move_index in solution_g2:
            input_perm = m.apply_single(input_perm, move.moves[move_index])

    if index_string(g3_strings, g3_string(input_perm)) > 95:
        solution_g3 = move.invert(move.translate(lookup_moves(g3_moves, index_string(g3_strings, g3_string(input_perm))), move.moves_g3))

        # bring input to g3:
        for move_index in solution_g3:
            input_perm = m.apply_single(input_perm, move.moves[move_index])

    if input_perm != 'uuuuuuuuffffffffllllllllbbbbbbbbrrrrrrrrdddddddd':
        solution_g4 = move.invert(move.translate(lookup_moves(g4_moves, index_string(g4_strings, g4_string(input_perm))), move.moves_g4))

        # bring input to g4:
        for move_index in solution_g4:
            input_perm = m.apply_single(input_perm, move.moves[move_index])

    # check if solution is correct
    if not input_perm == move.identity:
        return "ERROR"

    solution = move.cancel(move.cancel(move.cancel(solution_g1, solution_g2), solution_g3), solution_g4)
    return solution


print(move.moves_arduino(solve(m.apply(move.F, move.R2, move.L, move.U2, move.D, move.B2, move.F, move.R, move.L2, move.F, move.D2, move.R2))))
