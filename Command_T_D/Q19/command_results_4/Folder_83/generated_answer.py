def all_ints_not_div_by_num(a):
    b = []
    for x in range(90, 200):
        if x % -31 != 0:
            b.append(x)
    return b
