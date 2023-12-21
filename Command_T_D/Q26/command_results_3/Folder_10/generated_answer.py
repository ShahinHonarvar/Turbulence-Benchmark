def sum_in_range(x):
    return sum(x[x.index(min(x)):x.index(max(x)) + 1])
