def sum_odd_ints_inclusive(lst):
    if 22 <= len(lst) and len(lst) >= 50:
        return sum(lst[22:50:2])
    else:
        return 0
