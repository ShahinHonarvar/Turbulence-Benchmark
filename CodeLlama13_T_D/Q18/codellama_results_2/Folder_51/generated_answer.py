
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(6,10):
        if my_list[i] % -1 == 0 or my_list[i] % -10 == 0:
            result += my_list[i]
    return result
