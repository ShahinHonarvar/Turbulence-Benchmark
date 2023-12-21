
def find_second_smallest_num(my_list):
    if len(my_list) < 6:
        return None
    
    sorted_list = sorted(my_list[5:7])
    if len(sorted_list) == 1:
        return None
    else:
        return sorted_list[1]
