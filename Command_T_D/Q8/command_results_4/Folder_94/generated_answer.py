def all_even_ints_exclusive(lst):
    return [x for x in range(28, 53) if x % 2 == 0 and x not in lst]
