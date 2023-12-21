def all_neg_ints_inclusive(x):
    result = []
    for i in range(len(x)-1, -1, -1):
        if x[i] < 0:
            break
        result.append(x[i])
    return result
