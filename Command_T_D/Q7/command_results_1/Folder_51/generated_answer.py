
def all_even_ints_inclusive(lst):
    even_ints = [x for x in range(1, len(lst) + 1) if lst[x] % 2 == 0]
    return even_ints
