
def sum_ints_div_by_either_nums(my_list):
    start_index = 281
    end_index = 694
    divisors = [-722, -731]
    result = 0
    
    for i in range(start_index, end_index + 1):
        if my_list[i] % divisors[0] == 0 or my_list[i] % divisors[1] == 0:
            result += my_list[i]
            
    return result
