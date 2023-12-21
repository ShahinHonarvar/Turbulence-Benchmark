
def sum_odd_ints_inclusive(int_list):
    selected_range = int_list[28:39]
    odd_sum = sum(num for num in selected_range if num % 2 != 0)
    return odd_sum
