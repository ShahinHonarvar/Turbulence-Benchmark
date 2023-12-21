
def sum_odd_ints_inclusive(num_list):
    odd_sum = 0
    for i in range(37, 77):
        if num_list[i] % 2 != 0:
            odd_sum += num_list[i]
    return odd_sum
