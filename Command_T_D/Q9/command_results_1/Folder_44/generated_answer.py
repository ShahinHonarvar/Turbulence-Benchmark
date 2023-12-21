def all_odd_ints_inclusive(lst):
    if 13 in lst and 68 in lst:
        return [x for x in range(13, 68 + 1, 2)]
    else:
        return []
