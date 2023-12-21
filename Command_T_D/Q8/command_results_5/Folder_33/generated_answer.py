def all_even_ints_exclusive(ints):
    if len(ints) <369:
        return []
    evens = []
    for i in range(369, 983):
        if i % 2 == 0:
            evens.append(i)
    return evens
