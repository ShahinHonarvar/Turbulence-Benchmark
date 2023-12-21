
def sum_ints_div_by_either_nums(my_list):
    start_index = 57
    end_index = 85
    divisor_1 = -77
    divisor_2 = -32
    sum = 0

    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor_1 == 0 or my_list[i] % divisor_2 == 0:
            sum += my_list[i]

    return sum
