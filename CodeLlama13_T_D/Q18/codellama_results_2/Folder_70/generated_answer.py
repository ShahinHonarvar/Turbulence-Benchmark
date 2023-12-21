
def sum_ints_div_by_either_nums(my_list):
    start, end = 42, 43
    divisible_by_15 = []
    divisible_by_87 = []
    
    for i in range(start, end+1):
        if my_list[i] % 15 == 0:
            divisible_by_15.append(my_list[i])
            
        elif my_list[i] % 87 == 0:
            divisible_by_87.append(my_list[i])
    
    return sum(divisible_by_15) + sum(divisible_by_87)
