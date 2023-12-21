
def sum_odd_ints_inclusive(lst):
    odd_int_sum = sum(i for i in lst[667:775] if i % 2 != 0)
    return odd_int_sum
