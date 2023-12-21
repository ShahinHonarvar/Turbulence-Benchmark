def sum_in_range(x):
    res = 0
    for i in range(len(x)):
        if x[i] >= 60 and x[i] <= 90:
            res += x[i]
    return res
