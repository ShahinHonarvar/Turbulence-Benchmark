
def find_second_smallest_num(my_list):
    # Check if the input list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the input list in ascending order
    my_list.sort()

    # Initialize a variable to store the second smallest element
    second_smallest = None

    # Iterate through the elements of the sorted list starting from index 21 to index 97
    for i in range(20, 100):
        # Check if the current element is smaller than the previous smallest element
        if my_list[i] < second_smallest or second_smallest is None:
            # Update the variable to store the new second smallest element
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
