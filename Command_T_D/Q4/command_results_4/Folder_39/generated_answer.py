def all_pos_ints_exclusive(list):
    result = []
    for i in range(43, 99):
        if list[i] > 0:
            result.append(list[i])
    return result
