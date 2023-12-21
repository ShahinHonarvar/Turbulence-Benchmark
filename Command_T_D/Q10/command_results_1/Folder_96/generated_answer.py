def all_odd_ints_exclusive(lst):
    return [i for i in range(len(lst) - 1, -1, -2) if lst[i] % 2 == 1]
