
def sum_odd_ints_inclusive(int_list):
    sub_list = int_list[68:87]
    odd_int_sum = sum(x for x in sub_list if x % 2 != 0)
    return odd_int_sum
