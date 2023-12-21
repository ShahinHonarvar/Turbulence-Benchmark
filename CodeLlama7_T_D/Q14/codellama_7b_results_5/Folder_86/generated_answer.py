
def find_second_smallest_num(my_list):
    # Check if list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate through the list, starting from index 33
    for i in range(33, len(my_list)):
        # If the current element is smaller than the smallest element, update the smallest and second smallest elements
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        # If the current element is smaller than the second smallest element, update the second smallest element
        elif my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element from index 33 to index 36, both inclusive
    return second_smallest
