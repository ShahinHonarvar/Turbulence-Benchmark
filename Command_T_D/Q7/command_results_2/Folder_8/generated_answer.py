
def all_even_ints_inclusive(ints):
    even_ints = []
    for i in range(23, len(ints) + 1):
        if int(ints[i]) % 2 == 0:
            even_ints.append(ints[i])
    return even_ints
