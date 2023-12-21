
def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    if int_list[1] % 2 != 0:
        odd_sum += int_list[1]
    return odd_sum
