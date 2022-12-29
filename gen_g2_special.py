import move_tables as m


def move(string, move):
    result = ""
    for element in move:
        result += string[element]
    if move in [m.U, m.Up, m.D, m.Dp]:
        if string[48] == "0":
            result += "1"
        else:
            result += "0"
    else:
        result += string[48]
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


def gen_lookup():
    result = 0
    dist = [{'xxxxxxxxzfzzzfzzrrrrrrrryfzzzfzzrrrrrrrrxxxxxxxx0'}, {'xxxxxxxxyfzzzfzzrrrrrrrrzfzzzfzzrrrrrrrrxxxxxxxx0', 'xxxxxxxxrrrzzfzzyfzrrrrrrrrzzfzzzfzrrrrrxxxxxxxx1', 'xxxxxxxxzfzzyfzzrrrrrrrrzfzzzfzzrrrrrrrrxxxxxxxx0', 'xxxxxxxxzfzzzfzzrrrrrrrrzfzzyfzzrrrrrrrrxxxxxxxx0', 'xxxxxxxxzfzzrrrzrrrrzfzryfzzrrrzrrrrzfzrxxxxxxxx1', 'xxxxxxxxrrrzzfzzzfzrrrrrrrrzzfzzyfzrrrrrxxxxxxxx1'}]
    while dist[-1]:  # While latest set not empty
        print(len(dist[-1])) # Shows distribution
        result += len(dist[-1])
        dist.append(set())
        for pos in dist[-2]:
            for subpos in get_moves(pos):
                if is_new(subpos, dist):
                    dist[-1].add(subpos)
    print(result)
    print(len(dist) - 2)


lookup_moves = []
result = set(get_moves('xxxxxxxxzfzzzfzzrrrrrrrryfzzzfzzrrrrrrrrxxxxxxxx'))
result.remove('xxxxxxxxzfzzzfzzrrrrrrrryfzzzfzzrrrrrrrrxxxxxxxx')
print(result)
gen_lookup()
