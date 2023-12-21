
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    
    my_list = sorted(my_list)
    second_smallest = my_list[69]
    for i in range(70, 201):
        if my_list[i] == second_smallest:
            continue
        else:
            return my_list[i]
    
    return None
