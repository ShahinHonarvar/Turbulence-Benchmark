def all_odd_ints_exclusive(ints):
    return [i for i in range(4, len(ints)-1, 2) if ints[i] % 2 == 1]
