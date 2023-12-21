def all_even_ints_exclusive(lst):
    evens = [i for i in range(36, 85) if lst[i] % 2 == 0]
    return evens if len(evens) > 0 else []
