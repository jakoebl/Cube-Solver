import facelet_moves as m
import move_tables as tables
# Rotations

x = ['b5', 'b6', 'b7', 'b8', 'b1', 'b2', 'b3', 'b4',
     'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8',
     'l7', 'l8', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6',
     'd5', 'd6', 'd7', 'd8', 'd1', 'd2', 'd3', 'd4',
     'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r1', 'r2',
     'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8']

y = ['u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u1', 'u2',
     'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8',
     'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
     'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8',
     'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
     'd7', 'd8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6']

z = ['r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r1', 'r2',
     'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f1', 'f2',
     'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u1', 'u2',
     'b7', 'b8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6',
     'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd1', 'd2',
     'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l1', 'l2']


corner_facelets = ['u1', 'u3', 'u5' 'u7',
                   'f1', 'f3', 'f5', 'f7',
                   'l1', 'l3', 'l5', 'l7',
                   'b1', 'b3', 'b5', 'b7',
                   'r1', 'r3', 'r5', 'r7',
                   'd1', 'd3', 'd5', 'd7']

# cubies

UBL = ('u', 'l', 'b')
UBR = ('u', 'b', 'r')
UFL = ('u', 'f', 'l')
UFR = ('u', 'r', 'f')
DBL = ('d', 'b', 'l')
DBR = ('d', 'r', 'b')
DFL = ('d', 'l', 'f')
DFR = ('d', 'f', 'r')


def corner_clockwise_rotation(corner):
    return tuple([corner[2], corner[0], corner[1]])


def corners(perm):
    return [(perm[0], perm[16], perm[26]), (perm[2], perm[24], perm[34]), (perm[4], perm[32], perm[10]),
            (perm[6], perm[8], perm[18]), (perm[40], perm[20], perm[14]), (perm[42], perm[12], perm[38]),
            (perm[44], perm[36], perm[30]), (perm[46], perm[28], perm[22])]


corners_list = [UBL, UBR, UFR, UFL, DFL, DFR, DBR, DBL]

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


piece_index_g4 = ([('u', 'b'), ('u', 'r'), ('u', 'l', 'b'), ('f', 'r'), ('u', 'b', 'r')],
                  [('u', 'f'), ('u', 'l'), ('u', 'r', 'f'), ('f', 'l'), ('u', 'f', 'l')],
                  [('d', 'f'), ('d', 'r'), ('d', 'l', 'f'), ('b', 'l'), ('d', 'f', 'r')],
                  [('d', 'b'), ('d', 'l'), ('d', 'r', 'b'), ('b', 'r'), ('d', 'b', 'l')])


# pretty print is in "replaced by" notation
def pretty_print(perm):
    print("        ",                   perm[0], perm[1],   perm[2], "\n" +
          "        ",                   perm[7], "U ",      perm[3], "\n" +
          "        ",                   perm[6], perm[5],   perm[4], "\n" +
          perm[16], perm[17], perm[18], perm[8], perm[9],   perm[10], perm[32], perm[33], perm[34], "\n" +
          perm[23], "L ",     perm[19], perm[15], "F ",     perm[11], perm[39], "R ",     perm[35], "\n" +
          perm[22], perm[21], perm[20], perm[14], perm[13], perm[12], perm[38], perm[37], perm[36], "\n" +
          "        ",                   perm[40], perm[41], perm[42], "\n" +
          "        ",                   perm[47], "D ",     perm[43], "\n" +
          "        ",                   perm[46], perm[45], perm[44], "\n" +
          "        ",                   perm[28], perm[29], perm[30], "\n" +
          "        ",                   perm[27], "B ",     perm[31], "\n" +
          "        ",                   perm[26], perm[25], perm[24], "\n")
