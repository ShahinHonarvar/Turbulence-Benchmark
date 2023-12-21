
def sum_ints_div_by_either_nums(my_list):
    result = 0
    for i in range(18, 52+1):
        if my_list[i] % 15 == 0 or my_list[i] % 57 == 0:
            result += my_list[i]
    return result
