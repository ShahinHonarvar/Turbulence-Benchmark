
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second smallest element
    second_smallest = None
    second_smallest_index = -1

    # Iterate through the list from index 60 to index 200, both inclusive
    for i in range(60, 201):
        # If the current element is smaller than the second smallest element, update the variables accordingly
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest element from index 60 to index 200, both inclusive, or 'None' if there is no such an element
    return second_smallest if second_smallest_index != -1 else None
