
def all_even_ints_inclusive(lst):
    return [i for i in range(80, min(200, len(lst)), 2) if lst[i] % 2 == 0]
