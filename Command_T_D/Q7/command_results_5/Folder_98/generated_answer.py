
def all_even_ints_inclusive(ints):
    return [i for i in range(0, len(ints)) if int(ints[i]) % 2 == 0]
