def all_neg_ints_inclusive(x):
    result = []
    for i in range(50, 200):
        if x[i] < 0:
            result.append(x[i])
    return result
