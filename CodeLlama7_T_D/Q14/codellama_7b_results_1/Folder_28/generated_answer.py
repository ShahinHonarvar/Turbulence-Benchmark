
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    # Initialize variables for the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None
    # Iterate through the list starting from index 22 to index 50, both inclusive
    for i in range(22, 51):
        # Check if the current element is smaller than the smallest element
        if my_list[i] < smallest:
            # If it is, update the second smallest element with the smallest element and update the smallest element with the current element
            second_smallest = smallest
            smallest = my_list[i]
        # Check if the current element is smaller than the smallest element but greater than the second smallest element
        elif my_list[i] < smallest and my_list[i] > second_smallest:
            # If it is, update the second smallest element with the current element
            second_smallest = my_list[i]
    # Return the second smallest element if it exists, otherwise return None
    return second_smallest if second_smallest else None
