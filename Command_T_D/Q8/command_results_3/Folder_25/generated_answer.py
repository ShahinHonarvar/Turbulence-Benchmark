def all_even_ints_exclusive(lst):
    even_ints = list(range(40, 70, 2))
    return [x for x in even_ints if x in lst]
