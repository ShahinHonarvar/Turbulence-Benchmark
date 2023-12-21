
def find_second_smallest_num(my_list):
    # Check if the list has at least 25 elements
    if len(my_list) < 25:
        return None

    # Initialize a variable to store the second smallest element
    second_smallest = None

    # Iterate through the list starting from index 25
    for i in range(25, len(my_list)):
        # If the current element is smaller than the current second smallest element, update the second smallest element
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element if it exists, otherwise return 'None'
    return second_smallest
