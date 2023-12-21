
def all_even_ints_exclusive(lst):
    evens = []
    for i in range(2, 7):
        if lst[i] % 2 == 0:
            evens.append(lst[i])
    return evens
