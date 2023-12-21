def all_odd_ints_inclusive(lst):
    return [x for x in range(100, 200) if x % 2 == 1 and x in lst]
