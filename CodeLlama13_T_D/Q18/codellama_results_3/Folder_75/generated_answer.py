
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 20:
        return 0
    
    result = 0
    for i in range(20, 94):
        if my_list[i] % -92 == 0 or my_list[i] % -50 == 0:
            result += my_list[i]
            
    return result
