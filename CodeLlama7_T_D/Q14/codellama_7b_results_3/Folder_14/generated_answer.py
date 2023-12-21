
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variable to store second smallest element
    second_smallest = None

    # Iterate over elements from index 8 to index 9, both inclusive
    for i in range(8, 10):
        # Check if current element is smaller than the second smallest element
        if second_smallest is not None and my_list[i] < second_smallest:
            continue

        # If current element is smaller than the second smallest element or if there is no second smallest element yet, set it as the new second smallest element
        else:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
