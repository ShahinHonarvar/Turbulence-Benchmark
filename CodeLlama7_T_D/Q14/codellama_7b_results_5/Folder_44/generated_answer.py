
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list is empty

    if len(my_list) == 0:
        return None

    # Find the smallest element in the list

    smallest = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Return the second smallest element

    for i in range(len(my_list)):
        if my_list[i] == smallest:
            return my_list[i+1]

    # If there is no such an element, return None

    return None
