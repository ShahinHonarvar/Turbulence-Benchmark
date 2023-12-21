
def all_pos_ints_exclusive(ints):
    result = []
    for i in range(5, len(ints)):
        if ints[i] > 0:
            result.append(ints[i])
    return result
