 def find_second_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Check if there is a second smallest element
    if len(my_list) > 1:
        return my_list[1]
    else:
        return None
