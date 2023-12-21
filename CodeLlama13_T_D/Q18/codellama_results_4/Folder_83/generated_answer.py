
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(90, 201):
        if my_list[i] % -31 == 0 or my_list[i] % 13 == 0:
            result += my_list[i]
    return result
