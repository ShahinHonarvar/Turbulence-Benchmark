
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    
    sorted_list = sorted(my_list, reverse=True)
    second_largest = sorted_list[62]
    third_largest = sorted_list[63]
    
    if second_largest == third_largest:
        return None
    else:
        return second_largest
