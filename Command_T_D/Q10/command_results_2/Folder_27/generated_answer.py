def all_odd_ints_exclusive(lst):
    if not (28 <= len(lst) - 1 <= 49):
        return []
    return [i for i in range(len(lst) - 1, -1, 2) if lst[i] % 2 == 1]
