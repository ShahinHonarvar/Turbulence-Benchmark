def all_neg_ints_exclusive(lst):
    result = []
    for i in range(0, len(lst)):
        if lst[i] < 0:
            result.append(lst[i])
            break
    return result
