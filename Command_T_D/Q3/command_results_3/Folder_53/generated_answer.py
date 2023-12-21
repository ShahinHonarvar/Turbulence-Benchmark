def all_pos_ints_inclusive(list):
    result = []
    for i in range(100, 200):
        if i in list:
            result.append(i)
    return result
