
def all_even_ints_inclusive(ints):
    return [i for i in range(7, len(ints) + 7) if int(i) % 2 == 0]
