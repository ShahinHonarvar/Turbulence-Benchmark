
def sum_odd_ints_inclusive(my_list):
    start_index = 52
    end_index = 71
    odd_ints_sum = 0

    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_ints_sum += my_list[i]

    return odd_ints_sum
