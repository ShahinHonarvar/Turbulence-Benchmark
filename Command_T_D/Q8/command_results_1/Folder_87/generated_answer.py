def all_even_ints_exclusive(lst):
    return [i for i in range(32, 99) if i % 2 == 0 and i not in lst]
