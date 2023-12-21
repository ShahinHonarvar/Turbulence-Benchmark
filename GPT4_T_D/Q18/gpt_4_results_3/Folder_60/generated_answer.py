
def sum_ints_div_by_either_nums(a_list): 
    sum_of_nums = 0 
    for index in range(10, min(80,len(a_list))):
        if a_list[index] % -74 == 0 or a_list[index] % -58 == 0: 
            sum_of_nums += a_list[index] 
    return sum_of_nums
