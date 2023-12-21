
def all_pos_ints_exclusive(ints):
    result = []
    for i in range(94):
        if i > 93 and ints[i] > 0:
            result.append(ints[i])
    return result
