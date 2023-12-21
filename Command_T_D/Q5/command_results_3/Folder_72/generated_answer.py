def all_neg_ints_inclusive(list):
    result = []
    for i in range(29, 51):
        if list[i] < 0:
            result.append(list[i])
    return result
