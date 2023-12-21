def all_odd_ints_inclusive(lst):
    return [i for i in range(32, 36) if i & 1 and i in lst]
