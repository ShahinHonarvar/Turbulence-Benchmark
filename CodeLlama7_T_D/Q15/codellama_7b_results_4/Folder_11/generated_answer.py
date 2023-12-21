
def sum_odd_ints_inclusive(my_list):
    start_index = 37
    end_index = 51
    odd_int_sum = 0

    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_int_sum += my_list[i]

    return odd_int_sum
