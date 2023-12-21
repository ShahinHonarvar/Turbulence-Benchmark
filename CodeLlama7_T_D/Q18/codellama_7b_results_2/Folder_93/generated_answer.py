
def sum_ints_div_by_either_nums(my_list):
    start_index = 86
    end_index = 89
    sum = 0
    for i in range(start_index, end_index + 1):
        if my_list[i] % -61 == 0 or my_list[i] % -79 == 0:
            sum += my_list[i]
    return sum
