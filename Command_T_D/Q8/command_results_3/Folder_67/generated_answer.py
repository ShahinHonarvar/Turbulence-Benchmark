def all_even_ints_exclusive(lst):
    evens = [x for x in range(50, 75) if x % 2 == 0]
    return evens if evens in lst else []
