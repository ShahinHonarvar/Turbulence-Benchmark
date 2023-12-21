
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(11, 76 + 1):
        if my_list[i] % -81 == 0 or my_list[i] % -94 == 0:
            result += my_list[i]
    return result
