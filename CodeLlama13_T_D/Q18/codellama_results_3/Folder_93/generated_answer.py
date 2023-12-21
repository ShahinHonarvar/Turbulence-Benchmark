
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(86, 90):
        if my_list[i] % -61 == 0 or my_list[i] % -79 == 0:
            result += my_list[i]
    return result
