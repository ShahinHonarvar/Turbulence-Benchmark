
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 20 or len(my_list) > 93:
        return 0
    
    sum = 0
    for i in range(20, 94):
        if my_list[i] % -92 == 0 or my_list[i] % -50 == 0:
            sum += my_list[i]
    
    return sum
