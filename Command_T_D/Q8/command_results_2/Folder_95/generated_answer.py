def all_even_ints_exclusive(ints):
    evens = [e for e in range(25, 80) if e % 2 == 0]
    return [ints[i] for i in evens if ints[i] % 2 == 0]
