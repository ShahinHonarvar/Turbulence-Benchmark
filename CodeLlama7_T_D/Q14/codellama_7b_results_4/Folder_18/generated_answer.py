
def find_second_smallest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Initialize variables
    second_smallest = None
    smallest = my_list[0]

    # Iterate over the list and find the second smallest element
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        elif my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
