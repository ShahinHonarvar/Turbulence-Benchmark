
def find_second_smallest_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return None

    # Get the smallest element in the list
    smallest = my_list[0]

    # Initialize a variable to keep track of the second smallest element
    second_smallest = None

    # Iterate through the list and compare each element to the smallest element
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

    # If there is no such an element, return None
    if second_smallest is None:
        return None

    # Return the second smallest element
    return second_smallest
