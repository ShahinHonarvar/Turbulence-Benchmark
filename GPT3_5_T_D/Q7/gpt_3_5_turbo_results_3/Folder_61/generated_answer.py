
def all_even_ints_inclusive(lst):
    evens = []
    for i in range(7, 8):
        if lst[i] % 2 == 0:
            evens.append(lst[i])
    return evens
