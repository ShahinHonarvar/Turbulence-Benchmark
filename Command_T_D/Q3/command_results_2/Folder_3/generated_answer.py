def all_pos_ints_inclusive(list):
    result = []
    for i in range(len(list) - 1, -1, -1):
        if list[i] > 0:
            result.append(list[i])
            break
    return result
