# multiplication in "goes to" notation
# perm 2 is the 1st move
import move_tables as m


def apply_single(perm, move):
    i = 0
    result = []
    for num in range(48):
        result.append([])
    while i < 48:
        result[move[i]] = perm[i]
        i += 1
    return result


def inverse(move):
    return apply_single(apply_single(apply_single(m.identity, move), move), move)


def apply(*moves):
    result = m.identity
    for move in moves:
        result = apply_single(result, move)
    return result


def inv(*perms):
    result = apply(*perms)
    return inverse(result)
