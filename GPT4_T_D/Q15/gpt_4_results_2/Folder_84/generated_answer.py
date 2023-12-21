
def sum_odd_ints_inclusive(lst):
    odd_sum = sum(x for i, x in enumerate(lst[43:87]) if x % 2 != 0)
    return odd_sum
