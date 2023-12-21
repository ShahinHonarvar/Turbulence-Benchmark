
def all_ints_div_by_both_two_nums(lst):
    start_index = 828
    end_index = 932
    result = []
    
    for i in range(start_index, end_index + 1):
        if lst[i] % -649 == 0 and lst[i] % -461 == 0:
            result.append(lst[i])
    
    return result
