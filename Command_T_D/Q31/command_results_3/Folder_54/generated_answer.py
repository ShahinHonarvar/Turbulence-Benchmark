def if_perfect_num(x):
    return x[50] == sum(x[0:49]) == sum(x[0:49]) / float(len(x))
