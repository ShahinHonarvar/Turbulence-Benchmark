
def find_second_smallest_num(my_list):
    if len(my_list) < 20 or len(my_list) > 200:
        return None
    
    second_smallest = None
    for i in range(20, 201):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]
    
    return second_smallest
