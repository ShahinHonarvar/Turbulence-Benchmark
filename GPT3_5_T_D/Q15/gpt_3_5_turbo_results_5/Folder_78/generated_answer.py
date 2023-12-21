
def sum_odd_ints_inclusive(num_list):
    odd_sum = 0
    for num in num_list[43:52]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum
