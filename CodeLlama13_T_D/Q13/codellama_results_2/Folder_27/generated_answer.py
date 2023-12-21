
def find_second_largest_num(my_list):
    if len(my_list) < 66 or len(my_list) > 93:
        return None
    
    second_largest = my_list[65]
    for i in range(66, 94):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            
    return second_largest
