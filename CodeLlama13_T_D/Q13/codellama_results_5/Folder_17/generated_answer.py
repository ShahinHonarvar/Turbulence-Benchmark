
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list, reverse=True)
    second_largest_index = 62 + 17
    try:
        return sorted_list[second_largest_index]
    except IndexError:
        return None
