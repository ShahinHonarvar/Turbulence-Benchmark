def all_neg_ints_exclusive(lst):
    result = []
    for i in range(len(lst) - 1):
        if lst[i] < 0:
            result.append(lst[i])
        elif lst[i] > 0:
            break
    return result
