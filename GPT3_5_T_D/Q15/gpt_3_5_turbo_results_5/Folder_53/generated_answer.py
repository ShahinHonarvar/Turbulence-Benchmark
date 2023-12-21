
def sum_odd_ints_inclusive(lst):
    return sum([x for x in lst[300:301] if x % 2 != 0]) if any(x % 2 != 0 for x in lst[300:301]) else 0
