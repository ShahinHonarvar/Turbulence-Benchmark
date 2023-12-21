def all_neg_ints_exclusive(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] < 0:
            result.append(lst[i])
    return result
