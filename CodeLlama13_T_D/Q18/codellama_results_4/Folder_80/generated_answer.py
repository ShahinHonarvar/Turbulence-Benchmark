
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 93:
        return 0
    
    result = 0
    for i in range(14, 94):
        if my_list[i] % 71 == 0 or my_list[i] % 81 == 0:
            result += my_list[i]
            
    return result
