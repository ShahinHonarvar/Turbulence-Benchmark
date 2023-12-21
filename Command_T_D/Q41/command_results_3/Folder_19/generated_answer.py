def identical_elements(x, y):
    res = set()
    for i in range(len(x) - 2, len(x) - 1):
        if x[i] in y[i]:
            res.add(x[i])
    for j in range(len(y) - 2, len(y) - 1):
        if y[j] in x[j]:
            res.add(y[j])
    return res
