def all_even_ints_exclusive(ints):
    evens = []
    for i in range(len(ints)):
        if ints[i] % 2 == 0:
            evens.append(ints[i])
    return evens
