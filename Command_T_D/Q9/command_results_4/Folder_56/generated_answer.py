def all_odd_ints_inclusive(lst):
    return [n for n in range(0, len(lst)) if lst[n] % 2 == 1]
