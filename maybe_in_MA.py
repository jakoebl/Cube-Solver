# coordinate of 4! perms
def perm_coordinate_from_string(string):
    result = 0
    base = 1
    index = 1
    while index < len(string):
        digit_curr = 0
        for i in range(0, index):
            if int(string[index]) < int(string[i]):
                digit_curr += 1
        result += digit_curr * base
        base *= (index + 1)
        index += 1
    return int(result)