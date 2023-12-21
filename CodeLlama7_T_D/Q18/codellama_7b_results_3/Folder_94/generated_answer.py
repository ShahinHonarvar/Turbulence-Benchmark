
def sum_ints_div_by_either_nums(my_list):
    start_index = 93
    end_index = 94
    sum = 0

    for i in range(start_index, end_index + 1):
        if my_list[i] % -53 == 0 or my_list[i] % -91 == 0:
            sum += my_list[i]

    return sum
