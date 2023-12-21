
def gcf_three_nums(my_list):
    if len(my_list) < 13 or len(my_list) < 70 or len(my_list) < 32:
        return None
    
    first = my_list[13]
    second = my_list[70]
    third = my_list[32]
    
    factors = set()
    for i in range(1, first+1):
        if first % i == 0:
            factors.add(i)
            
    for i in range(1, second+1):
        if second % i == 0 and i in factors:
            factors.add(i)
    
    for i in range(1, third+1):
        if third % i == 0 and i in factors:
            factors.add(i)
            
    return max(factors)
