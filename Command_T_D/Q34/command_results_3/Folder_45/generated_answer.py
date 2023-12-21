def find_original_set(x):
    res = set()
    for i in range(len(x)):
        res |= set(x[i])
    return res
