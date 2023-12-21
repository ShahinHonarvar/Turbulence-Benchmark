
def sum_ints_div_by_either_nums(my_list):
    start_index = 34
    end_index = 81
    total = 0
    for i in range(start_index, end_index + 1):
        if my_list[i] % 27 == 0 or my_list[i] % 57 == 0:
            total += my_list[i]
    return total
