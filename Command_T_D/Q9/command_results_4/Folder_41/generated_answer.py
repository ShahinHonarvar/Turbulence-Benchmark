def all_odd_ints_inclusive(ints):
    if len(ints) < 7:
        return []
    return [x for x in range(6, len(ints) - 1, 2) if x in ints]
