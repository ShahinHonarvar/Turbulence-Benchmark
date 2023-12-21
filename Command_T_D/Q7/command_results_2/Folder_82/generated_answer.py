
def all_even_ints_inclusive(ints):
    evens = []
    for i in range(20, 200):
        if int(i) % 2 == 0:
            evens.append(ints[i])
    return evens
