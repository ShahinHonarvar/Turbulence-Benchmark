
def all_even_ints_inclusive(ints):
    return [i for i in range(len(ints) - 30, -1, -1) if i % 2 == 0]
