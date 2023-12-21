
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(78, 82):
        if my_list[i] % 76 == 0 or my_list[i] % 60 == 0:
            result += my_list[i]
    return result
