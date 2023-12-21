
def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    for i in range(25, 88):
        if i < len(int_list):
            if int_list[i] % 2 != 0:
                odd_sum += int_list[i]
    return odd_sum
