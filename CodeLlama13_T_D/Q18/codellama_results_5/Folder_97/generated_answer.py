
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(58, 76):
        if my_list[i] % 72 == 0 or my_list[i] % 62 == 0:
            result += my_list[i]
    return result
