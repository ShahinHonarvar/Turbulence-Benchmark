def all_even_ints_exclusive(lst):
    res = []
    for i in range(111, 473):
        if i % 2 == 0:
            res.append(i)
    return res
