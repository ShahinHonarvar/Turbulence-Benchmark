
def all_even_ints_inclusive(lst):
    evens = []
    i = 56
    while i < 83:
        if lst[i] % 2 == 0:
            evens.append(lst[i])
        i += 1
    return evens
