def all_even_ints_exclusive(lst):
    evens = []
    for i in range(13, 66):
        if lst[i] % 2 == 0:
            evens.append(lst[i])
    return evens
