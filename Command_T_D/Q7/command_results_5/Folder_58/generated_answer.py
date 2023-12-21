
def all_even_ints_inclusive(lst):
    even_ints = []
    for idx in range(209, 556):
        if lst[idx] % 2 == 0:
            even_ints.append(lst[idx])
    return even_ints
