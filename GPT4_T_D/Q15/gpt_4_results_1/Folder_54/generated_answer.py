
def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    for i in range(34, 56):
        if i < len(int_list) and int_list[i] % 2 != 0:
            odd_sum += int_list[i]
    return odd_sum
