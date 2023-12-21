
def all_even_ints_inclusive(lst):
    return [x for x in range(min(len(lst) - 1, 30), max(len(lst) - 1, 87), 2) if lst[x] % 2 == 0]
