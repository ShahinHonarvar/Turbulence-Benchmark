def all_odd_ints_exclusive(lst):
    return [i for i in range(1, 8) if i % 2 == 1 and i in lst]
