
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[13]
    for i in range(14, 69):
        if sorted_list[i] == second_smallest:
            continue
        else:
            return None
    
    return second_smallest
