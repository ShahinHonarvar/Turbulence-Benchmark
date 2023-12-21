def all_neg_ints_inclusive(lst):
    result = []
    for i in range(28, 38):
        if lst[i] < 0:
            result.append(lst[i])
    return result
