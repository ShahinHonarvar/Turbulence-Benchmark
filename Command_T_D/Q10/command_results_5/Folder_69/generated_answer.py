def all_odd_ints_exclusive(integers):
    if not integers:
        return []
    return [i for i in integers if i % 2 == 1 and i > 67 and i < 100]
