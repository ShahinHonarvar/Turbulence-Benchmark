
def all_even_ints_inclusive(lst):
    evens = []
    for i in range(len(lst) - 11):
        if lst[i] % 2 == 0:
            evens.append(lst[i])
    return evens
