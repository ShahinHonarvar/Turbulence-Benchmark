
def sum_odd_ints_inclusive(int_list):
    target_nums = int_list[50:55]
    odd_sum = sum(num for num in target_nums if num % 2 != 0)
    return odd_sum
