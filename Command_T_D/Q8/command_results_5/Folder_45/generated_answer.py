def all_even_ints_exclusive(lst):
    evens = [i for i in range(len(lst) - 30, -1, -2) if lst[i] % 2 == 0]
    return evens
