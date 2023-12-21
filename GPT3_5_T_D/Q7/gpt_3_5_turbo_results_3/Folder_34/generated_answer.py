
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(60, 201):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
