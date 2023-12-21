
def sum_odd_ints_inclusive(int_list):
    odd_sum = sum(val for ind, val in enumerate(int_list[19:93]) if val % 2 != 0)
    return odd_sum
