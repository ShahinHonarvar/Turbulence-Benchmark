
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(306, 958):
        if my_list[i] % 982 == 0 or my_list[i] % 319 == 0:
            result += my_list[i]
    return result
