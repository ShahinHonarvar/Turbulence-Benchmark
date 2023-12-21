def all_pos_ints_exclusive(integers):
    result = []
    for i in integers:
        if i >= 28 and i < 49:
            result.append(i)
    return result
