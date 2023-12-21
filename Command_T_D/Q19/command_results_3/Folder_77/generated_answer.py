def all_ints_not_div_by_num(x):
    result = []
    for i in range(668, 739):
        if x[i] % -172 != 0:
            result.append(x[i])
    return result
