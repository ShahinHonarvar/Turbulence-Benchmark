def sum_in_range(x):
    res = 0
    for i in x:
        if i >= 18 and i <= 60:
            res += i
    return res
