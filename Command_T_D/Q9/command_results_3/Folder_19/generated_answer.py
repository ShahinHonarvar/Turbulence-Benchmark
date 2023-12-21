def all_odd_ints_inclusive(lst):
    return [x for x in range(3, len(lst) - 1, 2) if lst[x] % 2 == 1]
