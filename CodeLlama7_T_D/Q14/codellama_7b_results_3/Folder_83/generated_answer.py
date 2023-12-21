
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Find the second smallest element
    for i in range(90, 201):
        if my_list[i] != my_list[i-1]:
            return my_list[i]

    # If there is no such an element, return 'None'
    return None
