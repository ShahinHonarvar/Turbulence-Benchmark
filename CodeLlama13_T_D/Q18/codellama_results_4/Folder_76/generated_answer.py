
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(250, 630):
        if my_list[i] % 850 == 0 or my_list[i] % 587 == 0:
            result += my_list[i]
    return result
