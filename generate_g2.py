import generate_UD
# 200: counter-clockwise rot
# 100: clockwise rot
# (all in relation to U and D)
# since we are in g1, F, Fp, B, and Bp are no longer needed
# strings: corners first, then edges
R_coord = (0, 102, 205, 3, 4, 106, 201, 7, 8, 16, 10, 11, 12, 19, 14, 15, 13, 17, 18, 9)
R2_coord = (0, 5, 6, 3, 4, 1, 2, 7, 8, 13, 10, 11, 12, 9, 14, 15, 19, 17, 18, 16)
Rp_coord = (0, 106, 201, 3, 4, 102, 205, 7, 8, 19, 10, 11, 12, 16, 14, 15, 9, 17, 18, 13)

F2_coord = (0, 1, 4, 5, 2, 3, 6, 7, 8, 9, 12, 11, 10, 13, 14, 15, 17, 16, 18, 19)

U_coord = (3, 0, 1, 2, 4, 5, 6, 7, 11, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19)
U2_coord = (2, 3, 0, 1, 4, 5, 6, 7, 10, 11, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19)
Up_coord = (1, 2, 3, 0, 4, 5, 6, 7, 9, 10, 11, 8, 12, 13, 14, 15, 16, 17, 18, 19)

L_coord = (207, 1, 2, 100, 203, 5, 6, 104, 8, 9, 10, 18, 12, 13, 14, 17, 16, 11, 15, 19)
L2_coord = (4, 1, 2, 7, 0, 5, 6, 3, 8, 9, 10, 15, 12, 13, 14, 11, 16, 18, 17, 19)
Lp_coord = (203, 1, 2, 104, 207, 5, 6, 100, 8, 9, 10, 17, 12, 13, 14, 18, 16, 15, 11, 19)

B2_coord = (6, 7, 2, 3, 4, 5, 0, 1, 14, 9, 10, 11, 12, 13, 8, 15, 16, 17, 19, 18)

D_coord = (0, 1, 2, 3, 7, 4,  5, 6, 8, 9, 10, 11, 15, 12, 13, 14, 16, 17, 18, 19)
D2_coord = (0, 1, 2, 3, 6, 7, 4, 5, 8, 9, 10, 11, 14, 15, 12, 13, 16, 17, 18, 19)
Dp_coord = (0, 1, 2, 3, 5, 6, 7, 4, 8, 9, 10, 11, 13, 14, 15, 12, 16, 17, 18, 19)

# moves for UD slice
R_flip = (0, 4, 2, 3, 9, 5, 6, 1, 8, 7, 10, 11)
R2_flip = (0, 9, 2, 3, 7, 5, 6, 4, 8, 1, 10, 11)
Rp_flip = (0, 7, 2, 3, 1, 5, 6, 9, 8, 4, 10, 11)

F2_flip = (0, 1, 8, 3, 5, 4, 6, 7, 2, 9, 10, 11)

U_flip = (3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11)
U2_flip = (2, 3, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11)
Up_flip = (1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11)

L_flip = (0, 1, 2, 6, 4, 3, 11, 7, 8, 9, 10, 5)
L2_flip = (0, 1, 2, 11, 4, 6, 5, 7, 8, 9, 10, 3)
Lp_flip = (0, 1, 2, 5, 4, 11, 3, 7, 8, 9, 10, 6)

B2_flip = (10, 1, 2, 3, 4, 5, 7, 6, 8, 9, 0, 11)

D_flip = (0, 1, 2, 3, 4, 5, 6, 7, 11, 8, 9, 10)
D2_flip = (0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 8, 9)
Dp_flip = (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8)

moves = [U_coord, Up_coord, U2_coord, F2_coord, L_coord, Lp_coord, L2_coord,
         B2_coord, R_coord, Rp_coord, R2_coord, D_coord, Dp_coord, D2_coord]

moves_ed = [U_flip, Up_flip, U2_flip, F2_flip, L_flip, Lp_flip, L2_flip,
            B2_flip, R_flip, Rp_flip, R2_flip, D_flip, Dp_flip, D2_flip]


lookup_coord_to_str_UD_slice = generate_UD.lookup_string


# takes coord and flip_move
def move(string, move):  # coordinate int
    result = ""
    for element in move:
        if element < 100:
            result += string[element]
        else:
            if element > 199:  # counter-clockwise flip
                result += str((int(string[element % 100]) + 2) % 3)
            else:  # clockwise flip
                result += str((int(string[element % 100]) + 1) % 3)
    return result


# convert back to coordinate from 7 bit ternary string
def co_coordinate_from_string(string):
    exponent = 6
    result = 0
    for bit in string:
        if bit == "1":
            result += 3 ** exponent
        elif bit == "2":
            result += 2 * 3 ** exponent
        exponent -= 1
        if exponent == -1:
            break
    return result


# convert back to coordinate from 12 bit binary string
def ed_coordinate_from_string(string):
    return lookup_coord_to_str_UD_slice.index(string)


def coordinate(string):
    return ed_coordinate_from_string(string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14] + string[15] + string[16] + string[17] + string[18] + string[19]) + 495 * co_coordinate_from_string(string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7])


# applies all moves to string form of a coordinate and stores the converted result in a set
def get_moves(string):
    result = list()
    for element in moves:
        result.append(move(string, element))
    return tuple(result)


# generates empty lookup list with 495 sublists (3 ** 7 elements each)
def gen_empty_lookup_g2():
    for index in range(1082565):
        lookup_g2.append("")
    lookup_g2[coordinate('20012001000100011001')] = [4]
    lookup_g2[coordinate('01200120010001000110')] = [8]


def is_new(pos, distribution):
    for depth in distribution:
        if pos in depth:
            return False
    return True


def gen_lookup_g2():
    dist = [{"00000000000000001111"}, {'20012001000100011001', '01200120010001000110'}]
    gen_empty_lookup_g2()
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1]))  # Shows distribution
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if is_new(subpos, dist):
                    dist[-1].add(subpos)
                    temp = []
                    for index in range(len(lookup_g2[coordinate(pos)])):
                        temp.append(lookup_g2[coordinate(pos)][index])
                    temp.append(get_moves(pos).index(subpos))
                    lookup_g2[coordinate(subpos)] = temp


# writes lookup for g2 to file
def write_lookup(file):
    gen_empty_lookup_g2()
    gen_lookup_g2()
    table_g2 = open(file, "w")
    for lists in lookup_g2:
        for element in lists:
            table_g2.write(str(element))
            table_g2.write(" ")
        table_g2.write("\n")
    table_g2.close()

