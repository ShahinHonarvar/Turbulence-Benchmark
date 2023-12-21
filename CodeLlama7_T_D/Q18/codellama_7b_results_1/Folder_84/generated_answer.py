
def sum_ints_div_by_either_nums(my_list):
    start_index = 78
    end_index = 81
    sum = 0

    for i in range(start_index, end_index + 1):
        if my_list[i] % 76 == 0 or my_list[i] % 60 == 0:
            sum += my_list[i]

    return sum
