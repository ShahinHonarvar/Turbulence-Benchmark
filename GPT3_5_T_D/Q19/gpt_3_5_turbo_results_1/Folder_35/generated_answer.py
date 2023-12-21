
def all_ints_not_div_by_num(lst):
    divisor = 86
    start_index = 15
    end_index = 57
    result = []
    
    for i in range(start_index, end_index):
        if lst[i] % divisor != 0:
            result.append(lst[i])
    
    return result
