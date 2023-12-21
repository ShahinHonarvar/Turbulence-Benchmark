def all_odd_ints_inclusive(lst):
    res = [y for y in range(10, 100, 2) if y in lst]
    return res
