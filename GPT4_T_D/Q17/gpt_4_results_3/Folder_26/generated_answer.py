
def all_ints_div_by_both_two_nums(lst):
    result = []
    
    for i in lst[69:71]:
        if (i % 72 == 0 and i % 70 == 0):
            result.append(i)
        
    return result
