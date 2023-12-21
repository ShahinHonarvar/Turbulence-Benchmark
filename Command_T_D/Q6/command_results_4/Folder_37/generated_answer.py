def all_neg_ints_exclusive(a):
    result = []
    i = 1
    j = 2
    while j < len(a):
        if a[i] < 0:
            result.append(a[i])
        i += 1
        j += 1
    return result
