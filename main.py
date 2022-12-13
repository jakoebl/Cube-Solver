# Identity

identity = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8',
            'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
            'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8',
            'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
            'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8',
            'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8']

co_no_buffer = ['u1', 'u3', 'u7',
                'f1', 'f5', 'f7',
                'l1', 'l3', 'l5', 'l7',
                'b1', 'b3', 'b5', 'b7',
                'r3', 'r5', 'r7',
                'd1', 'd3', 'd5', 'd7']

co_w_buffer = ['u1', 'u3', 'u5' 'u7',
               'f1', 'f3', 'f5', 'f7',
               'l1', 'l3', 'l5', 'l7',
               'b1', 'b3', 'b5', 'b7',
               'r1', 'r3', 'r5', 'r7',
               'd1', 'd3', 'd5', 'd7']

# cubies

UBL = ('u1', 'b3', 'l1')
UBR = ('u3', 'b1', 'r3')
UFL = ('u7', 'f1', 'l3')
UFR = ('u5', 'f3', 'r1')
DBL = ('d7', 'b5', 'l7')
DBR = ('d5', 'b7', 'r5')
DFL = ('d1', 'f7', 'l5')
DFR = ('d3', 'f5', 'r7')

cubies = [UBL, UBR, UFR, UFL, DFL, DFR, DBR, DBL]
# Moves

U = ['u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u1', 'u2',
     'l1', 'l2', 'l3', 'f4', 'f5', 'f6', 'f7', 'f8',
     'b1', 'b2', 'b3', 'l4', 'l5', 'l6', 'l7', 'l8',
     'r1', 'r2', 'r3', 'b4', 'b5', 'b6', 'b7', 'b8',
     'f1', 'f2', 'f3', 'r4', 'r5', 'r6', 'r7', 'r8',
     'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8']

U_PR = ['u7', 'u8', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6',
        'r1', 'r2', 'r3', 'f4', 'f5', 'f6', 'f7', 'f8',
        'f1', 'f2', 'f3', 'l4', 'l5', 'l6', 'l7', 'l8',
        'l1', 'l2', 'l3', 'b4', 'b5', 'b6', 'b7', 'b8',
        'b1', 'b2', 'b3', 'r4', 'r5', 'r6', 'r7', 'r8',
        'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8']

U2 = ['u5', 'u6', 'u7', 'u8', 'u1', 'u2', 'u3', 'u4',
      'b1', 'b2', 'b3', 'f4', 'f5', 'f6', 'f7', 'f8',
      'r1', 'r2', 'r3', 'l4', 'l5', 'l6', 'l7', 'l8',
      'f1', 'f2', 'f3', 'b4', 'b5', 'b6', 'b7', 'b8',
      'l1', 'l2', 'l3', 'r4', 'r5', 'r6', 'r7', 'r8',
      'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8']

F = ['u1', 'u2', 'u3', 'u4', 'r7', 'r8', 'r1', 'u8',
     'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f1', 'f2',
     'l1', 'l2', 'u5', 'u6', 'u7', 'l6', 'l7', 'l8',
     'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
     'd3', 'r2', 'r3', 'r4', 'r5', 'r6', 'd1', 'd2',
     'l3', 'l4', 'l5', 'd4', 'd5', 'd6', 'd7', 'd8']

F_PR = ['u1', 'u2', 'u3', 'u4', 'l3', 'l4', 'l5', 'u8',
        'f7', 'f8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
        'l1', 'l2', 'd1', 'd2', 'd3', 'l6', 'l7', 'l8',
        'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
        'u7', 'r2', 'r3', 'r4', 'r5', 'r6', 'u5', 'u6',
        'r7', 'r8', 'r1', 'd4', 'd5', 'd6', 'd7', 'd8']

F2 = ['u1', 'u2', 'u3', 'u4', 'd1', 'd2', 'd3', 'u8',
      'f5', 'f6', 'f7', 'f8', 'f1', 'f2', 'f3', 'f4',
      'l1', 'l2', 'r7', 'r8', 'r1', 'l6', 'l7', 'l8',
      'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
      'l5', 'r2', 'r3', 'r4', 'r5', 'r6', 'l3', 'l4',
      'u5', 'u6', 'u7', 'd4', 'd5', 'd6', 'd7', 'd8']

L = ['f1', 'u2', 'u3', 'u4', 'u5', 'u6', 'f7', 'f8',
     'd1', 'f2', 'f3', 'f4', 'f5', 'f6', 'd7', 'd8',
     'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l1', 'l2',
     'b1', 'b2', 'u7', 'u8', 'u1', 'b6', 'b7', 'b8',
     'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8',
     'b5', 'd2', 'd3', 'd4', 'd5', 'd6', 'b3', 'b4']

L_PR = ['b5', 'u2', 'u3', 'u4', 'u5', 'u6', 'b3', 'b4',
        'u1', 'f2', 'f3', 'f4', 'f5', 'f6', 'u7', 'u8',
        'l7', 'l8', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6',
        'b1', 'b2', 'd7', 'd8', 'd1', 'b6', 'b7', 'b8',
        'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8',
        'f1', 'd2', 'd3', 'd4', 'd5', 'd6', 'f7', 'f8']

L2 = ['d1', 'u2', 'u3', 'u4', 'u5', 'u6', 'd7', 'd8',
      'b5', 'f2', 'f3', 'f4', 'f5', 'f6', 'b3', 'b4',
      'l5', 'l6', 'l7', 'l8', 'l1', 'l2', 'l3', 'l4',
      'b1', 'b2', 'f7', 'f8', 'f1', 'b6', 'b7', 'b8',
      'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8',
      'u1', 'd2', 'd3', 'd4', 'd5', 'd6', 'u7', 'u8']

B = ['l7', 'l8', 'l1', 'u4', 'u5', 'u6', 'u7', 'u8',
     'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
     'd7', 'l2', 'l3', 'l4', 'l5', 'l6', 'd5', 'd6',
     'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b1', 'b2',
     'r1', 'r2', 'u1', 'u2', 'u3', 'r6', 'r7', 'r8',
     'd1', 'd2', 'd3', 'd4', 'r3', 'r4', 'r5', 'd8']

B_PR = ['r3', 'r4', 'r5', 'u4', 'u5', 'u6', 'u7', 'u8',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
        'u3', 'l2', 'l3', 'l4', 'l5', 'l6', 'u1', 'u2',
        'b7', 'b8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6',
        'r1', 'r2', 'd5', 'd6', 'd7', 'r6', 'r7', 'r8',
        'd1', 'd2', 'd3', 'd4', 'l7', 'l8', 'l1', 'd8']

B2 = ['d5', 'd6', 'd7', 'u4', 'u5', 'u6', 'u7', 'u8',
      'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
      'r5', 'l2', 'l3', 'l4', 'l5', 'l6', 'r3', 'r4',
      'b5', 'b6', 'b7', 'b8', 'b1', 'b2', 'b3', 'b4',
      'r1', 'r2', 'l7', 'l8', 'l1', 'r6', 'r7', 'r8',
      'd1', 'd2', 'd3', 'd4', 'u1', 'u2', 'u3', 'd8']

R = ['u1', 'u2', 'b7', 'b8', 'b1', 'u6', 'u7', 'u8',
     'f1', 'f2', 'u3', 'u4', 'u5', 'f6', 'f7', 'f8',
     'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8',
     'd5', 'b2', 'b3', 'b4', 'b5', 'b6', 'd3', 'd4',
     'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r1', 'r2',
     'd1', 'd2', 'f3', 'f4', 'f5', 'd6', 'd7', 'd8']

R_PR = ['u1', 'u2', 'f3', 'f4', 'f5', 'u6', 'u7', 'u8',
        'f1', 'f2', 'd3', 'd4', 'd5', 'f6', 'f7', 'f8',
        'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8',
        'u5', 'b2', 'b3', 'b4', 'b5', 'b6', 'u3', 'u4',
        'r7', 'r8', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6',
        'd1', 'd2', 'b7', 'b8', 'b1', 'd6', 'd7', 'd8']

R2 = ['u1', 'u2', 'd3', 'd4', 'd5', 'u6', 'u7', 'u8',
      'f1', 'f2', 'b7', 'b8', 'b1', 'f6', 'f7', 'f8',
      'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8',
      'f5', 'b2', 'b3', 'b4', 'b5', 'b6', 'f3', 'f4',
      'r5', 'r6', 'r7', 'r8', 'r1', 'r2', 'r3', 'r4',
      'd1', 'd2', 'u3', 'u4', 'u5', 'd6', 'd7', 'd8']

D = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8',
     'f1', 'f2', 'f3', 'f4', 'r5', 'r6', 'r7', 'f8',
     'l1', 'l2', 'l3', 'l4', 'f5', 'f6', 'f7', 'l8',
     'b1', 'b2', 'b3', 'b4', 'l5', 'l6', 'l7', 'b8',
     'r1', 'r2', 'r3', 'r4', 'b5', 'b6', 'b7', 'r8',
     'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd1', 'd2']

D_PR = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8',
        'f1', 'f2', 'f3', 'f4', 'l5', 'l6', 'l7', 'f8',
        'l1', 'l2', 'l3', 'l4', 'b5', 'b6', 'b7', 'l8',
        'b1', 'b2', 'b3', 'b4', 'r5', 'r6', 'r7', 'b8',
        'r1', 'r2', 'r3', 'r4', 'f5', 'f6', 'f7', 'r8',
        'd7', 'd8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6']

D2 = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8',
      'f1', 'f2', 'f3', 'f4', 'b5', 'b6', 'b7', 'f8',
      'l1', 'l2', 'l3', 'l4', 'r5', 'r6', 'r7', 'l8',
      'b1', 'b2', 'b3', 'b4', 'f5', 'f6', 'f7', 'b8',
      'r1', 'r2', 'r3', 'r4', 'l5', 'l6', 'l7', 'r8',
      'd5', 'd6', 'd7', 'd8', 'd1', 'd2', 'd3', 'd4']

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

# Lists
moves = [U, U_PR, U2, F, F_PR, F2, L, L_PR, L2, B, B_PR, B2, R, R_PR, R2, D, D_PR, D2]


# multiplication in "goes to" notation
# list 2 is the 1st move
def multiplication(perm1, perm2):
    i = 0
    result = []
    while i < 48:
        result.append(perm1[identity.index(perm2[i])])
        i += 1
    return result


def inverse(perm):
    i = 0
    result = []
    while i < 48:
        result.append(identity[perm.index(identity[i])])
        i += 1
    return result


def mult(*perms):
    result = identity
    for perm in perms:
        result = multiplication(perm, result)
    return result


def inv(*perms):
    result = mult(*perms)
    return inverse(result)


def corners(*perms):
    perm = mult(*perms)
    result = []
    i = 0
    while i < 48:
        result.append(perm[i])
        i += 2
    return result


def edges(*perms):
    perm = mult(*perms)
    result = []
    i = 1
    while i < 48:
        result.append(perm[i])
        i += 2
    return result


# pretty print is in "replaced by" notation
def pretty_print(*perm_goes_to):
    perm = inv(*perm_goes_to)
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


# 2x2 brute force:
def coord_co(*perms):
    perm = corners(mult(*perms))
    coord_or = 0
    exp = 729
    for element in ['u1', 'u3', 'u5', 'u7', 'd1', 'd3', 'd5']:
        if perm.index(element) in [0, 1, 2, 3, 20, 21, 22, 23]:
            exp /= 3
        elif perm.index(element) in [4, 6, 8, 10, 12, 14, 16, 18]:
            coord_or += exp
            exp /= 3
        else:
            coord_or += exp * 2
            exp /= 3

    coord_perm = 0
    # find order of cubies
    perm_rp = corners(inv(*perms))
    order = []
    perm_reduced = []
    for num in [0, 1, 2, 3, 20, 21, 22, 23]:
        perm_reduced.append(perm_rp[num])

    for facelet in perm_reduced:
        for cubie in cubies:
            if facelet in cubie:
                order.append(cubie[0])
    # define natural order
    order_nat = ['u1', 'u3', 'u5', 'u7', 'd1', 'd3', 'd5', 'd7']
    test = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 1
    j = 0
    base = 1
    while i < 8:
        while j < i:
            if order_nat.index(order[j]) > order_nat.index(order[i]):  # find facelets of higher order left of facelet
                coord_perm += 1 * base
                test[i] += 1
            j += 1
        j = 0
        i += 1
        base *= i
    return coord_or, coord_perm


def lal():
    corners_lookup = []
    i = 0
    j = 0
    while i < 37321:
        corners_lookup.append([])
        while j < 2186:
            corners_lookup[i].append([])
            j += 1
        i += 1
        j = 0
        print(i)
    print("success")
    print(corners_lookup)
    print(len(corners_lookup))
    for element in corners_lookup:
        print(len(element))


lal()
