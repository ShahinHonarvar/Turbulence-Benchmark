def sum_in_range(lst):
    res = 0
    for i in lst:
        if i >= -97 and i <= -48:
            res += i
    return res
