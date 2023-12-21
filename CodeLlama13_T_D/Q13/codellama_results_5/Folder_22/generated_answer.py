
def find_second_largest_num(my_list):
    if len(my_list) <= 2:
        return None
    
    second_largest = None
    for i in range(40, 201):
        current = my_list[i]
        if current > second_largest:
            second_largest = current
            
    return second_largest
