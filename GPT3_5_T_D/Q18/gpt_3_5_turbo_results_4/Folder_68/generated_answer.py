
def sum_ints_div_by_either_nums(integers):
    result = 0
    
    for i in range(7, 8):
        if integers[i] % 5 == 0 or integers[i] % 7 == 0:
            result += integers[i]
    
    return result
