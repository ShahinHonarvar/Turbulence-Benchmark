
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(28, 97):
        if my_list[i] % 90 == 0 or my_list[i] % 97 == 0:
            result += my_list[i]
    return result
