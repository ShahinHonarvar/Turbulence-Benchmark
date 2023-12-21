def all_odd_ints_inclusive(lst):
    return [x for x in range(6, len(lst) + 1, 2) if x in lst]
