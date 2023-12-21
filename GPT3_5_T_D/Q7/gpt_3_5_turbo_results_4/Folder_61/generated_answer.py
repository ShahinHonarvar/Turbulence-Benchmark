
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(7, 8):
        if i >= len(lst):
            return even_ints
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
