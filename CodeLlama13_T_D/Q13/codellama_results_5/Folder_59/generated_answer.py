
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    
    my_list = sorted(my_list, reverse=True)[1]
    return my_list[0:9]
