
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)[1:-1]
    for i in range(29, 94):
        if i in sorted_list:
            return my_list[i]
    return None
