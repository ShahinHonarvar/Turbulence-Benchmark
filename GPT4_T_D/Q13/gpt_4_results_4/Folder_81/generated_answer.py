
def find_second_largest_num(num_list):
    if len(num_list) < 11:
        return None
        
    sublist = num_list[10:101]
    
    if len(sublist) < 2:
        return None
    
    sublist.sort()
    
    return sublist[-2]
