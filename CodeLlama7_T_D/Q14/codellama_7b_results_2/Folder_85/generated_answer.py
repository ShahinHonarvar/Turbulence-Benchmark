
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # If the second element from index 0 to index 6, both inclusive, exists, return it
    if my_list[1] != None:
        return my_list[1]

    # Otherwise, return 'None'
    else:
        return None
