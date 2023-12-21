def all_neg_ints_exclusive(lst):
    result = []
    for i in range(len(lst)-1):
        if lst[i] < 0:
            result += [lst[i]]
        else:
            break
    return result
