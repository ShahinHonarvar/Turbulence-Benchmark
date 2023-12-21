
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[1]
    
    for i in range(2, len(sorted_list)):
        if sorted_list[i] == second_smallest:
            continue
        
        if sorted_list[i] < second_smallest:
            second_smallest = sorted_list[i]
    
    return second_smallest
