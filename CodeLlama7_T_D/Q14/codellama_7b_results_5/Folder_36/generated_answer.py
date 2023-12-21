
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second smallest element
    second_smallest = None
    current_index = 209

    # Iterate through the list and find the second smallest element
    for i in range(len(my_list)):
        if my_list[i] < my_list[current_index]:
            second_smallest = my_list[i]

    # Return the second smallest element, or None if it could not be found
    return second_smallest
