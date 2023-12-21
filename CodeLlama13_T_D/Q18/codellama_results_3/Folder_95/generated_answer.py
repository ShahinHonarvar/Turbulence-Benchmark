
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(57,85):
        if my_list[i] % -30 == 0 or my_list[i] % -88 == 0:
            result += my_list[i]
    return result
