
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(24, 33):
        if my_list[i] % 35 == 0 or my_list[i] % 87 == 0:
            result += my_list[i]
    return result
