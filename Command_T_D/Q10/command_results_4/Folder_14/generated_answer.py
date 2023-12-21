def all_odd_ints_exclusive(lst):
    return [i for i in range(1, len(lst) + 1) if lst[i - 1] % 2 == 1]
