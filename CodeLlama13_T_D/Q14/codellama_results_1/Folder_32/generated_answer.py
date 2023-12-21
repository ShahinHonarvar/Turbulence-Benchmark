
def find_second_smallest_num(my_list):
    # sort the list in ascending order
    my_list.sort()
    
    # check if there is a second smallest element between index 32 to 35, both inclusive
    if len(my_list) < 35:
        return None
    else:
        for i in range(32, 36):
            if my_list[i] != my_list[i-1]:
                return my_list[i-1]
        return None
