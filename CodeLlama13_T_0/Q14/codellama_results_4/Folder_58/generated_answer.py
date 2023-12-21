
def find_second_smallest_num(my_list):
    if len(my_list) < 310 or len(my_list) > 370:
        return None
    
    second_smallest = my_list[310]
    for i in range(311, 371):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
            
    return second_smallest
