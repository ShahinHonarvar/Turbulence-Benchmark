def all_neg_ints_inclusive(ints):
    result = []
    for i in range(20, min(len(ints), 200)):
        if ints[i] < 0:
            result.append(ints[i])
    return result
