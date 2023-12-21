def all_ints_not_div_by_num(x):
    x = list(range(x[0], x[1] + 1))
    return [x[i] for i in range(len(x)) if not x[i] % 7]
