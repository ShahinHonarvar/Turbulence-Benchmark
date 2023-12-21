def sum_odd_ints_inclusive(lst):
    return sum(i for i in range(max(lst[63:66]), lst[64], 2) if i in lst)
