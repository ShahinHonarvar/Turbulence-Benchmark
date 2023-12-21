
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    
    my_list.sort()
    for i in range(1, len(my_list)):
        if my_list[i] == my_list[i - 1]:
            continue
        else:
            return my_list[i]
