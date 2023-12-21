def all_odd_ints_exclusive(lst):
    return [x for x in range(64, 81) if x % 2 == 1 and x in lst]
