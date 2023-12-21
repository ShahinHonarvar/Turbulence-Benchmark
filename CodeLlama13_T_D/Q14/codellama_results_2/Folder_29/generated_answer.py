
def find_second_smallest_num(my_list):
    if len(my_list) < 98:
        return None
    
    my_list = sorted(my_list[55:99])
    second_smallest = my_list[1]
    
    return second_smallest
