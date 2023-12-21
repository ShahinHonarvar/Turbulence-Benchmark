
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)[1:-1]
    if len(sorted_list) == 0:
        return None
    
    second_largest_num = sorted_list[len(sorted_list) // 2]
    return second_largest_num
