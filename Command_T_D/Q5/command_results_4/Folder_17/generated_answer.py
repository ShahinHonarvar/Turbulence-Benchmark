def all_neg_ints_inclusive(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        if lst[i] < 0:
            result.append(lst[i])
    return result
