def all_odd_ints_exclusive(lst):
    odds = [n for n in range(40, 200, 2) if lst[n - 1] % 2 == 1]
    return [lst[i] for i in odds if lst[i] % 2 == 1]
