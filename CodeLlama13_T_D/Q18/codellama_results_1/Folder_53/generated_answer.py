
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(200, 201):
        if my_list[i] % 17 == 0 or my_list[i] % -5 == 0:
            result += my_list[i]
    return result
