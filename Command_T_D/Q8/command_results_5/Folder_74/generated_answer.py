def all_even_ints_exclusive(lst):
    evens = [i for i in range(13, 70, 2) if lst[i] % 2 == 0]
    return evens if evens else []
