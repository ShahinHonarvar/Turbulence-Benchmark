
def find_second_smallest_num(my_list):
    if len(my_list) <= 1:
        return None
    
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[639]
    
    for i in range(640, 975+1):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
            
    return second_smallest
