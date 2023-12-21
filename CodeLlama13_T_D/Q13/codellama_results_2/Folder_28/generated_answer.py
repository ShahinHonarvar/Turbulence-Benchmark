
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)[-2:]
    for i in range(62, 64):
        if sorted_list[i] is not None:
            return sorted_list[i]
    return None
