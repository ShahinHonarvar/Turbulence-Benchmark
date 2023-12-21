
def find_second_largest_num(my_list):
    if len(my_list) <= 2:
        return None
    
    sorted_list = sorted(my_list)[1:-1]
    second_largest = sorted_list[50]
    
    for i in range(49, -1, -1):
        if sorted_list[i] > second_largest:
            return None
            
        if sorted_list[i] < second_largest:
            second_largest = sorted_list[i]
    
    return second_largest
