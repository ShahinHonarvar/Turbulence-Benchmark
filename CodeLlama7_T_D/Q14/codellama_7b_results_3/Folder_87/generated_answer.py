
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second smallest number and its index
    second_smallest = None
    second_smallest_index = -1

    # Iterate through the list from index 22 to index 88, both inclusive
    for i in range(22, 90):
        # If the current element is smaller than the second smallest number, update the second smallest number and its index
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest number from index 22 to index 88, both inclusive
    return second_smallest
