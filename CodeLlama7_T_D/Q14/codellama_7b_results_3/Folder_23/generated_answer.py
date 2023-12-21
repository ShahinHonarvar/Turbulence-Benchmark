
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # Check if the list is empty

    if len(my_list) == 0:
        return None

    # Sort the list in ascending order

    my_list.sort()

    # Initialize variables to keep track of the second smallest element and its index

    second_smallest = None

    second_smallest_index = -1

    # Iterate through the list starting from index 19 to index 92 (both inclusive)

    for i in range(19, 93):

        # If the current element is smaller than the second smallest element, update the second smallest element and its index

        if second_smallest is not None and my_list[i] < second_smallest:
            second_smallest = my_list[i]

            second_smallest_index = i

    # Return the second smallest element from index 19 to index 92 (both inclusive) or 'None' if there is no such an element

    return second_smallest if second_smallest_index != -1 else None
