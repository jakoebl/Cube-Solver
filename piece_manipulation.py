def corner_clockwise_rotation(corner):
    return tuple([corner[2], corner[0], corner[1]])


def corners(perm):
    return [(perm[0], perm[16], perm[26]), (perm[2], perm[24], perm[34]), (perm[4], perm[32], perm[10]),
            (perm[6], perm[8], perm[18]), (perm[40], perm[20], perm[14]), (perm[42], perm[12], perm[38]),
            (perm[44], perm[36], perm[30]), (perm[46], perm[28], perm[22])]


def corner_parity(corners):
    result = 0
    for i in range(0, 7):
        for j in range(i + 1, 8):
            result ^= bool(corners_solved.index(corners[i]) > corners_solved.index(corners[j]))
    return result


corners_solved = [('u', 'l', 'b'), ('u', 'b', 'r'), ('u', 'r', 'f'), ('u', 'f', 'l'), ('d', 'l', 'f'), ('d', 'f', 'r'), ('d', 'r', 'b'), ('d', 'b', 'l')]


# edges
def flip(edge):
    return tuple([edge[1], edge[0]])


def edges(perm):
    return [(perm[1], perm[25]), (perm[3], perm[33]), (perm[5], perm[9]), (perm[7], perm[17]),
            (perm[11], perm[39]), (perm[15], perm[19]), (perm[27], perm[23]), (perm[31], perm[35]),
            (perm[41], perm[13]), (perm[43], perm[37]), (perm[45], perm[29]), (perm[47], perm[21])]


edges_solved = [('u', 'b'), ('u', 'r'), ('u', 'f'), ('u', 'l'), ('f', 'r'), ('f', 'l'),
                ('b', 'l'), ('b', 'r'), ('d', 'f'), ('d', 'r'), ('d', 'b'), ('d', 'l')]

m_slice = [('u', 'b'), ('u', 'f'), ('d', 'f'), ('d', 'b')]

s_slice = [('u', 'r'), ('u', 'l'), ('d', 'r'), ('d', 'l')]

# whole cube
solved_cube = ([('u', 'b'), ('u', 'r'), ('u', 'l', 'b'), ('f', 'r'), ('u', 'b', 'r')],
               [('u', 'f'), ('u', 'l'), ('u', 'r', 'f'), ('f', 'l'), ('u', 'f', 'l')],
               [('d', 'f'), ('d', 'r'), ('d', 'l', 'f'), ('b', 'l'), ('d', 'f', 'r')],
               [('d', 'b'), ('d', 'l'), ('d', 'r', 'b'), ('b', 'r'), ('d', 'b', 'l')])


def pretty_print(perm):
    print("     ",                   perm[0], perm[1],   perm[2], "\n" +
          "     ",                   perm[7], "U",       perm[3], "\n" +
          "     ",                   perm[6], perm[5],   perm[4], "\n" +
          perm[16], perm[17], perm[18], perm[8], perm[9],   perm[10], perm[32], perm[33], perm[34], "\n" +
          perm[23], "L",      perm[19], perm[15], "F",      perm[11], perm[39], "R",      perm[35], "\n" +
          perm[22], perm[21], perm[20], perm[14], perm[13], perm[12], perm[38], perm[37], perm[36], "\n" +
          "     ",                   perm[40], perm[41], perm[42], "\n" +
          "     ",                   perm[47], "D",      perm[43], "\n" +
          "     ",                   perm[46], perm[45], perm[44], "\n" +
          "     ",                   perm[28], perm[29], perm[30], "\n" +
          "     ",                   perm[27], "B",      perm[31], "\n" +
          "     ",                   perm[26], perm[25], perm[24], "\n")
