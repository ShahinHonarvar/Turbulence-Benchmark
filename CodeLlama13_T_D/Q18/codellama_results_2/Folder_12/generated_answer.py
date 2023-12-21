
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(35, 64+1):
        if my_list[i] % -30 == 0 or my_list[i] % -95 == 0:
            result += my_list[i]
    return result
