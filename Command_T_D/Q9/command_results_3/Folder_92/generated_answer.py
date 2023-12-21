def all_odd_ints_inclusive(lst):
    return [i for i in range(0, len(lst) + 1) if lst[i] % 2]
