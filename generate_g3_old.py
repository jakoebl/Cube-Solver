import generate_8C4
# UBL cycle is 1, S slice is 1, BL and BR are 1
# corners first, standard order, then edges, U layer, then D layer, then E slice
R2_coord = (0, 5, 6, 3, 4, 1, 2, 7, 8, 13, 10, 11, 12, 9, 14, 15, 19, 17, 18, 16)

F2_coord = (0, 1, 4, 5, 2, 3, 6, 7, 8, 9, 12, 11, 10, 13, 14, 15, 17, 16, 18, 19)

U_coord = (3, 0, 1, 2, 4, 5, 6, 7, 11, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19)
U2_coord = (2, 3, 0, 1, 4, 5, 6, 7, 10, 11, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19)
Up_coord = (1, 2, 3, 0, 4, 5, 6, 7, 9, 10, 11, 8, 12, 13, 14, 15, 16, 17, 18, 19)

L2_coord = (4, 1, 2, 7, 0, 5, 6, 3, 8, 9, 10, 15, 12, 13, 14, 11, 16, 18, 17, 19)

B2_coord = (6, 7, 2, 3, 4, 5, 0, 1, 14, 9, 10, 11, 12, 13, 8, 15, 16, 17, 19, 18)

D_coord = (0, 1, 2, 3, 7, 4,  5, 6, 8, 9, 10, 11, 15, 12, 13, 14, 16, 17, 18, 19)
D2_coord = (0, 1, 2, 3, 6, 7, 4, 5, 8, 9, 10, 11, 14, 15, 12, 13, 16, 17, 18, 19)
Dp_coord = (0, 1, 2, 3, 5, 6, 7, 4, 8, 9, 10, 11, 13, 14, 15, 12, 16, 17, 18, 19)

moves = [U_coord, Up_coord, U2_coord, F2_coord, L2_coord,
         B2_coord, R2_coord, D_coord, Dp_coord, D2_coord]

moves_g4 = [U2_coord, F2_coord, L2_coord, B2_coord, R2_coord, D2_coord]


def move(string, move):  # coordinate int
    result = ""
    for element in move:
        result += string[element]
    if move in [U_coord, Up_coord, D_coord, Dp_coord]:
        if string[20] == "0":
            result += "1"
        else:
            result += "0"
    else:
        result += string[20]
    return result


def order_corners(string):
    corner_list = []
    for index in range(8):
        corner_list.append(string[index])
    ordered_list = []
    for i in range(4):
        ordered_list.append(corner_list.index(str(i)))
    ordered_list.sort()
    for num in range(4):
        ordered_list[num] = corner_list[ordered_list[num]]
    for n in range(8):
        corner_list[n] = ordered_list.index(corner_list[n])
    result = ""
    for element in corner_list:
        result += str(element)
    return result


def coordinate_4C2(string):
    lookup_4C2 = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}]
    return lookup_4C2.index({int(string[1]), int(string[0])})


def coordinate(string):
    result = generate_8C4.lookup.index(string[0] + string[2] + string[4] + string[6] + string[1] + string[3] + string[5] + string[7])
    result += 70 * generate_8C4.lookup.index(string[8] + string[10] + string[12] + string[14] + string[9] + string[11] + string[13] + string[15])
    result += 70 ** 2 * coordinate_4C2(string[16] + string[17])
    return result


def get_moves(string):
    result = list()
    for element in moves:
        result.append(move(string, element))
    return tuple(result)


def is_new(pos, distribution):
    for depth in distribution:
        if pos in depth:
            return False
    return True


def gen_lookup():
    dist = [{'0167452301010101xxxx0', '2561074301010101xxxx0', '0563274101010101xxxx0', '0743612501010101xxxx0', '2301456701010101xxxx0', '4307612501010101xxxx0', '2165034701010101xxxx0', '4163270501010101xxxx0', '0365214701010101xxxx0', '2561430701010101xxxx0', '0365472101010101xxxx0', '0347216501010101xxxx0', '4765032101010101xxxx0', '4567012301010101xxxx0', '2507614301010101xxxx0', '6745230101010101xxxx0', '2147036501010101xxxx0', '4703216501010101xxxx0', '2345670101010101xxxx0', '2507436101010101xxxx0', '2741056301010101xxxx0', '4721036501010101xxxx0', '4361250701010101xxxx0', '2367014501010101xxxx0', '0123674501010101xxxx0', '6521470301010101xxxx0', '0123456701010101xxxx0', '6125430701010101xxxx0', '4721650301010101xxxx0', '0167234501010101xxxx0', '6107432501010101xxxx0', '4703652101010101xxxx0', '6723014501010101xxxx0', '2103476501010101xxxx0', '0563412701010101xxxx0', '4325076101010101xxxx0', '4163052701010101xxxx0', '0541276301010101xxxx0', '4105276301010101xxxx0', '6327410501010101xxxx0', '6143250701010101xxxx0', '2543610701010101xxxx0', '6327054101010101xxxx0', '4765210301010101xxxx0', '2345016701010101xxxx0', '4523670101010101xxxx0', '0321654701010101xxxx0', '0725436101010101xxxx0', '6125074301010101xxxx0', '6503214701010101xxxx0', '2301674501010101xxxx0', '6701452301010101xxxx0', '2705416301010101xxxx0', '0347652101010101xxxx0', '0725614301010101xxxx0', '4523016701010101xxxx0', '0145672301010101xxxx0', '2741630501010101xxxx0', '2103654701010101xxxx0', '2705634101010101xxxx0', '2763054101010101xxxx0', '0321476501010101xxxx0', '0145236701010101xxxx0', '2367450101010101xxxx0', '0527634101010101xxxx0', '6107254301010101xxxx0', '6305412701010101xxxx0', '6341270501010101xxxx0', '4105632701010101xxxx0', '6701234501010101xxxx0', '0761254301010101xxxx0', '6503472101010101xxxx0', '4307256101010101xxxx0', '2763410501010101xxxx0', '2165470301010101xxxx0', '4361072501010101xxxx0', '6143072501010101xxxx0', '6547210301010101xxxx0', '4567230101010101xxxx0', '0541632701010101xxxx0', '6521034701010101xxxx0', '0527416301010101xxxx0', '6723450101010101xxxx0', '6745012301010101xxxx0', '4325610701010101xxxx0', '6341052701010101xxxx0', '4127630501010101xxxx0', '4501236701010101xxxx0', '4127056301010101xxxx0', '0743256101010101xxxx0', '0761432501010101xxxx0', '4501672301010101xxxx0', '6547032101010101xxxx0', '2147650301010101xxxx0', '2543076101010101xxxx0', '6305274101010101xxxx0'}]
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1]))  # Shows distribution
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if is_new(subpos, dist):
                    dist[-1].add(subpos)
                    lookup_strings.append(subpos)
                    lookup_moves.append(lookup_moves[lookup_strings.index(pos)] + [get_moves(pos).index(subpos)])


def write_lookup(file):
    gen_lookup()
    table_g3 = open(file, "w")
    for lists in lookup:
        for element in lists:
            table_g3.write(str(element))
            table_g3.write(" ")
        table_g3.write("\n")
    table_g3.close()


lookup_moves = []
for num in range(96):
    lookup_moves.append([])
lookup_strings = ['0167452301010101xxxx0', '2561074301010101xxxx0', '0563274101010101xxxx0', '0743612501010101xxxx0', '2301456701010101xxxx0', '4307612501010101xxxx0', '2165034701010101xxxx0', '4163270501010101xxxx0', '0365214701010101xxxx0', '2561430701010101xxxx0', '0365472101010101xxxx0', '0347216501010101xxxx0', '4765032101010101xxxx0', '4567012301010101xxxx0', '2507614301010101xxxx0', '6745230101010101xxxx0', '2147036501010101xxxx0', '4703216501010101xxxx0', '2345670101010101xxxx0', '2507436101010101xxxx0', '2741056301010101xxxx0', '4721036501010101xxxx0', '4361250701010101xxxx0', '2367014501010101xxxx0', '0123674501010101xxxx0', '6521470301010101xxxx0', '0123456701010101xxxx0', '6125430701010101xxxx0', '4721650301010101xxxx0', '0167234501010101xxxx0', '6107432501010101xxxx0', '4703652101010101xxxx0', '6723014501010101xxxx0', '2103476501010101xxxx0', '0563412701010101xxxx0', '4325076101010101xxxx0', '4163052701010101xxxx0', '0541276301010101xxxx0', '4105276301010101xxxx0', '6327410501010101xxxx0', '6143250701010101xxxx0', '2543610701010101xxxx0', '6327054101010101xxxx0', '4765210301010101xxxx0', '2345016701010101xxxx0', '4523670101010101xxxx0', '0321654701010101xxxx0', '0725436101010101xxxx0', '6125074301010101xxxx0', '6503214701010101xxxx0', '2301674501010101xxxx0', '6701452301010101xxxx0', '2705416301010101xxxx0', '0347652101010101xxxx0', '0725614301010101xxxx0', '4523016701010101xxxx0', '0145672301010101xxxx0', '2741630501010101xxxx0', '2103654701010101xxxx0', '2705634101010101xxxx0', '2763054101010101xxxx0', '0321476501010101xxxx0', '0145236701010101xxxx0', '2367450101010101xxxx0', '0527634101010101xxxx0', '6107254301010101xxxx0', '6305412701010101xxxx0', '6341270501010101xxxx0', '4105632701010101xxxx0', '6701234501010101xxxx0', '0761254301010101xxxx0', '6503472101010101xxxx0', '4307256101010101xxxx0', '2763410501010101xxxx0', '2165470301010101xxxx0', '4361072501010101xxxx0', '6143072501010101xxxx0', '6547210301010101xxxx0', '4567230101010101xxxx0', '0541632701010101xxxx0', '6521034701010101xxxx0', '0527416301010101xxxx0', '6723450101010101xxxx0', '6745012301010101xxxx0', '4325610701010101xxxx0', '6341052701010101xxxx0', '4127630501010101xxxx0', '4501236701010101xxxx0', '4127056301010101xxxx0', '0743256101010101xxxx0', '0761432501010101xxxx0', '4501672301010101xxxx0', '6547032101010101xxxx0', '2147650301010101xxxx0', '2543076101010101xxxx0', '6305274101010101xxxx0']
gen_lookup()

strings = open("strings_g3", "w")
moves = open("moves_g3", "w")
for element in lookup_strings:
    strings.write(element)
    strings.write("\n")
for element in lookup_moves:
    for mov in element:
        moves.write(str(mov) + " ")
    moves.write("\n")
