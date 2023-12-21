
def sum_odd_ints_inclusive(int_list):
    odd_ints_sum = sum(num for i, num in enumerate(int_list[209:557]) if num % 2 != 0)
    return odd_ints_sum
