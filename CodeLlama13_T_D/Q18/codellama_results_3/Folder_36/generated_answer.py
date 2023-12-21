
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(299, 383):
        if my_list[i] % 858 == 0 or my_list[i] % 952 == 0:
            result += my_list[i]
    return result
