def all_odd_ints_inclusive(lst):
    return [i for i in range(3, len(lst) - 1, 2) if lst[i] % 2 == 1]
