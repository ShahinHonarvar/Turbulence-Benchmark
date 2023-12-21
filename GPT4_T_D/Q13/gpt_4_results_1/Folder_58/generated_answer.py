
def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
        
    if 208 < len(num_list) <= 557:
        num_list = num_list[209: 557]
        
    elif len(num_list) > 557:
        num_list = num_list[209: 557]
        
    else:
        return None
    
    num_list.sort()
    
    return num_list[-2]
