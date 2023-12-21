
def find_second_largest_num(my_list):
    if len(my_list) < 4:
        return None
    
    sorted_list = sorted(my_list)[-4:]
    second_largest = sorted_list[1]
    
    for i in range(33, 37):
        if my_list[i] == second_largest:
            return my_list[i]
    
    return None
