def all_odd_ints_exclusive(lst):
    if not lst:
        return []
    for i in range(13, 67):
        if lst[i] % 2 == 1:
            yield lst[i]
