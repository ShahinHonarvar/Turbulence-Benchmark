
def sum_odd_ints_inclusive(lst):
    return sum(filter(lambda x: x % 2 != 0, lst[22:51])) if any(x % 2 != 0 for x in lst[22:51]) else 0
