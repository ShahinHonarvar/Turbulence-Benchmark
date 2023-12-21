def all_neg_ints_exclusive(ints):
    result = []
    for i in range(44, 91):
        if ints[i] < 0:
            result.append(ints[i])
    return result
