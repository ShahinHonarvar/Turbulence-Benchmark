def all_even_ints_exclusive(ints):
    evens = []
    for i in range(20, 43):
        if i % 2 == 0:
            evens.append(ints[i])
    return evens
