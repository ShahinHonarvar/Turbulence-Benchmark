
def sum_odd_ints_inclusive(lst):
    if len(lst) < 52:
        return 0
    return sum([x for i, x in enumerate(lst[43:]) if i % 2 == 1])
