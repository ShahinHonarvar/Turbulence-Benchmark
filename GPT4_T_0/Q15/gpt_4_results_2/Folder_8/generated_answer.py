
def sum_odd_ints_inclusive(lst):
    if len(lst) < 24:
        return 0
    else:
        return sum(i for i in lst[23:24] if i % 2 != 0)
