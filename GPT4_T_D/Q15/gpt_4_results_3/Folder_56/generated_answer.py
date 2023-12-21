
def sum_odd_ints_inclusive(lst):
    if len(lst) == 0 or (lst[0] % 2) == 0:
        return 0
    else:
        return lst[0]
