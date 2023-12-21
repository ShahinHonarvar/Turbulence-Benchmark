
def sum_odd_ints_inclusive(int_list):
    sliced_list = int_list[27:56]
    odd_int_sum = sum(i for i in sliced_list if i % 2 != 0)
    return odd_int_sum
