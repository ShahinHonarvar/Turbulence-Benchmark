def all_pos_ints_inclusive(ints):
    result = []
    for i in range(22, 63):
        try:
            result.append(ints[i])
        except IndexError:
            break
    return result
