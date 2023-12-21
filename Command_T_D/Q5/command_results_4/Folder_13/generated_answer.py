def all_neg_ints_inclusive(lst):
    result = []
    for i in range(25, 87):
        if lst[i] < 0:
            result.append(lst[i])
    return result
