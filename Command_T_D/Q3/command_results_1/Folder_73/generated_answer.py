def all_pos_ints_inclusive(lst):
    result = []
    for i in range(19, 93):
        if i in lst:
            result.append(i)
    return result
