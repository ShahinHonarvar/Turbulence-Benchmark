
def find_second_smallest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second smallest element and its index
    second_smallest = None
    second_smallest_index = -1

    # Iterate through the list and find the second smallest element
    for i in range(40, 201):
        if my_list[i] < second_smallest or second_smallest == None:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest element and its index
    return (second_smallest, second_smallest_index)
