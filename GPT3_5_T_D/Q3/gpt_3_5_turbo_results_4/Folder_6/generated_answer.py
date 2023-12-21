
def all_pos_ints_inclusive(lst):
    result = []
    for i in range(10, 67):
        if lst[i] > 0:
            result.append(lst[i])
    return result
