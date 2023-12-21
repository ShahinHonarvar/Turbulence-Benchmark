def sum_odd_ints_inclusive(lst):
    return sum(x for x in lst[686::2] if x%2==1)
