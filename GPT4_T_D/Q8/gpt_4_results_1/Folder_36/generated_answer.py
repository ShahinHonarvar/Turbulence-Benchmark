
def all_even_ints_exclusive(lst):
    even_integers = []
    for i in range(599, 767):
        if lst[i] % 2 == 0:
            even_integers.append(lst[i])
    return even_integers
