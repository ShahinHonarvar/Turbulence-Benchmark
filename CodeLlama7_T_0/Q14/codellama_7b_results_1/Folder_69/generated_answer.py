
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second smallest element
    second_smallest = None
    current_index = 25

    # Iterate through the list and find the second smallest element
    for i in range(current_index, len(my_list)):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
