
def sum_odd_ints_inclusive(int_list):
    subset_list = int_list[246:751]
    odd_int_sum = sum(i for i in subset_list if i % 2 != 0)
    return odd_int_sum
