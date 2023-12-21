def all_neg_ints_exclusive(lst):
    result = []
    for i in range(1, len(lst) + 1):
        if lst[i - 1] < 0:
            result.append(lst[i - 1])
            break
    return result
