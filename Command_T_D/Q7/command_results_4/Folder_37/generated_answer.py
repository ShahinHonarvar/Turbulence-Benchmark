
def all_even_ints_inclusive(ints):
    even_ints = []
    for i in range(1, len(ints) + 1):
        if int(ints[i - 1]) % 2 == 0:
            even_ints += [ints[i - 1]]
        if int(ints[i]) % 2 == 0:
            even_ints += [ints[i]]
    return even_ints
