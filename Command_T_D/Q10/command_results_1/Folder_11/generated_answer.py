def all_odd_ints_exclusive(lst):
    return [x for x in range(15, 99) if x % 2 == 1 and x in lst]
