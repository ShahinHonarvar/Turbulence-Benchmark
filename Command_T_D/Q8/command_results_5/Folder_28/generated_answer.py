def all_even_ints_exclusive(lst):
    return [x for x in range(20, 52) if x % 2 == 0 and x in lst]
