def all_odd_ints_inclusive(ints):
    if len(ints) < 40 or 200 < len(ints) - 40:
        return []
    return [x for x in range(40, 200, 2) if x in ints]
