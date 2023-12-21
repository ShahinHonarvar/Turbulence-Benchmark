
def all_even_ints_exclusive(lst):
    even_ints = []
    for i in range(20, 35):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
