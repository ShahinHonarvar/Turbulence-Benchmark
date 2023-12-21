def all_even_ints_exclusive(ints):
    evens = []
    for i in range(69, 97):
        if (ints[i] % 2) == 0:
            evens.append(ints[i])
    return evens
