def all_even_ints_exclusive(lst):
    evens = [x for x in range(20, 37) if x % 2 == 0]
    return [x for x in lst if x in evens]
