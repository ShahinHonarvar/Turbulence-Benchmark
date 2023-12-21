
def find_second_smallest_num(my_list):
    if len(my_list) < 5:
        return None
    
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[4]
    for i in range(4, len(sorted_list)):
        if sorted_list[i] != second_smallest:
            break
        
    return second_smallest
