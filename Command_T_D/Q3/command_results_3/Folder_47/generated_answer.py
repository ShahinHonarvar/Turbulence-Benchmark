def all_pos_ints_inclusive(lst):
    result = []
    for i in range(37, len(lst) + 1):
        if lst[i] > 0:
            result.append(lst[i])
    return result
