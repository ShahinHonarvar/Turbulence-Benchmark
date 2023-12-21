
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[15:40]
    
    if not second_smallest:
        return None
    else:
        return second_smallest[0]
