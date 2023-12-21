
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(50, 93):
        if my_list[i] % -94 == 0 or my_list[i] % -95 == 0:
            result += my_list[i]
    return result
