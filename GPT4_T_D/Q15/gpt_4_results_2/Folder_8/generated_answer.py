
def sum_odd_ints_inclusive(lst):
    if len(lst) >= 24:
        sublist = lst[23:24]
        return sum([i for i in sublist if i % 2 != 0])
    else:
        return 0
