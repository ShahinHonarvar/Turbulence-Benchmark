
def find_second_largest_num(my_list):
    if len(my_list) <= 1:
        return None
    
    sorted_list = sorted(my_list)[90:91]
    if not sorted_list:
        return None
    else:
        return sorted_list[0]
