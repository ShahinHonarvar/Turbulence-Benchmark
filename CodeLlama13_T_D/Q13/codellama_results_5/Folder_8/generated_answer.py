
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list, reverse=True)
    second_largest = sorted_list[1]
    
    for i in range(23, 24):
        if my_list[i] == second_largest:
            return second_largest
    
    return None
