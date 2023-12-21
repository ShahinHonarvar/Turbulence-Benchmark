
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(29, 54):
        if my_list[i] % -68 == 0 or my_list[i] % -85 == 0:
            result += my_list[i]
    return result
